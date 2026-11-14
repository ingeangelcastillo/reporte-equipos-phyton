# Reporte de equipos instalados - por ingeangelcastillo

equipos = [
    {"equipo": "Detector de humo", "marca": "System Sensor", "ubicacion": "Piso 1"},
    {"equipo": "Cámara PTZ", "marca": "Hikvision", "ubicacion": "Estacionamiento"},
    {"equipo": "Panel de alarma", "marca": "Notifier", "ubicacion": "Cuarto de control"},
]

print("=== REPORTE DE EQUIPOS INSTALADOS ===")
for e in equipos:
    print(f"{e['equipo']} - {e['marca']} - {e['ubicacion']}")

print(f"\nTotal de equipos: {len(equipos)}")
print("Reporte generado por ingeangelcastillo")
