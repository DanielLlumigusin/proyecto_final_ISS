import unittest
from ataques.detectar_ataques import detectar_ddos, detectar_escaneo_puertos
from scapy.all import IP, TCP

class TestDeteccionAtaques(unittest.TestCase):

    def test_deteccion_ddos(self):
        paquete = IP(src="192.168.0.10")/TCP(sport=12345, dport=80)
        self.assertTrue(detectar_ddos(paquete))

    def test_deteccion_escaneo(self):
        paquete = TCP(dport=80)
        self.assertTrue(detectar_escaneo_puertos(paquete))

if __name__ == '__main__':
    unittest.main()
