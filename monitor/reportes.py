import json
import os

REPORTE_FILE = 'reporte_ataques.json'

def generar_reporte(ataque):
    """Genera un reporte de ataque y lo guarda en un archivo."""
    reporte = {
        'origen': ataque['origen'],
        'tipo': ataque['tipo'],
        'fecha': ataque['fecha'],
        'severidad': ataque['severidad']
    }
    with open(REPORTE_FILE, 'a') as file:
        json.dump(reporte, file)
        file.write('\n')

def obtener_reportes():
    """Obtiene los reportes de ataques desde el archivo."""
    if not os.path.exists(REPORTE_FILE):
        return []
    
    reportes = []
    with open(REPORTE_FILE, 'r') as file:
        for line in file:
            reportes.append(json.loads(line))
    return reportes
