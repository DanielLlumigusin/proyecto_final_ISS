from scapy.layers.inet import IP, TCP

direcciones_ip = []
umbral_ddos = 100

def detectar_ddos(paquete):
    if IP in paquete:
        ip_origen = paquete[IP].src
        if ip_origen not in direcciones_ip:
            direcciones_ip.append(ip_origen)
        if len(direcciones_ip) > umbral_ddos:
            return True
    return False

def detectar_escaneo_puertos(paquete):
    if TCP in paquete:
        puerto_destino = paquete[TCP].dport
        # Agregar lógica para detectar escaneo de puertos.
        return True
    return False
