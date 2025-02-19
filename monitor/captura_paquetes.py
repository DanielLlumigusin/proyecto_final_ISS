import scapy.all as scapy
from monitor.analisis_red import analizar_ataques

def capturar_paquetes(interface):
    """Captura paquetes en la red."""
    scapy.sniff(iface=interface, store=0, prn=analizar_paquete)

def analizar_paquete(paquete):
    """Analiza el paquete capturado y detecta ataques."""
    resultado = analizar_ataques(paquete)
    if resultado:
        print(f"Ataque detectado: {resultado}")
