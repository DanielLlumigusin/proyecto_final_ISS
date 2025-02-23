import scapy.all as scapy
from monitor.analisis_red import analizar_ataques

paquetes_capturados = []
paquetes_analizados = []

def capturar_paquetes(interface):
    """Captura paquetes en la red."""
    resultado = scapy.sniff(iface=interface, store=0, prn=analizar_paquete)
    if resultado not null:
        print(f"Paquete Capturado, {resultado}")
        paquetes_capturados.append(resultado)
        return paquetes_capturados

def analizar_paquete(paquete):
    """Analiza el paquete capturado y detecta ataques."""
    resultado = analizar_ataques(paquete)
    if resultado:
        print(f"Ataque detectado: {resultado}")
        paquetes_analizados.append(resultado)
        return paquetes_analizados