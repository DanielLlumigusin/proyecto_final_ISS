from flask import Blueprint, render_template
from monitor.reportes import obtener_reportes
from monitor.captura_paquetes import capturar_paquetes
import threading

main = Blueprint('main', __name__)

@main.route('/')
def index():
    ataques = obtener_ataques_en_tiempo_real()
    return render_template('index.html', ataques=ataques)

@main.route('/capturar')
def capturar():
    interface = "Ethernet"
    iniciar_captura(interface)
    return render_template('captura.html', mensaje="Captura de paquetes iniciada.", paquetes=capturar_paquetes)

@main.route('/reportes')
def reportes():
    reportes = obtener_reportes()
    return render_template('report.html', reportes=reportes)

def obtener_ataques_en_tiempo_real():
    # Lógica para obtener ataques en tiempo real
    return [
        {'id': 1, 'tipo': 'DDoS', 'origen': '192.168.0.1'},
        {'id': 2, 'tipo': 'Escaneo de puertos', 'origen': '192.168.0.2'}
    ]

def iniciar_captura(interface):
    """Inicia la captura de paquetes en un hilo separado."""
    thread = threading.Thread(target=capturar_paquetes, args=(interface,))
    thread.daemon = True  
    thread.start()