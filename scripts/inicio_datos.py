import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gestor.gestor_jugadores import menu_alta_jugadores

if __name__ == "__main__":
    menu_alta_jugadores()

