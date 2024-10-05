import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vista')))

from Ventana import crear_ventana_pantalla_completa

print("Programa ejecutado")
crear_ventana_pantalla_completa()
print("Fin programa")