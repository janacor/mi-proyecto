import json
import os

RUTA_JSON = 'equipos.json'

# ---------------------------
# Funciones de carga y guardado
# ---------------------------
def cargar_equipos():
    if not os.path.exists(RUTA_JSON):
        with open(RUTA_JSON, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=4, ensure_ascii=False)
    with open(RUTA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_equipos(equipos):
    with open(RUTA_JSON, 'w', encoding='utf-8') as f:
        json.dump(equipos, f, indent=4, ensure_ascii=False)

# ---------------------------
# Funciones de gestión
# ---------------------------
def alta_equipo(nombre_equipo):
    equipos = cargar_equipos()
    if nombre_equipo in equipos:
        print(f"El equipo '{nombre_equipo}' ya existe.")
    else:
        equipos[nombre_equipo] = {"jugadores": []}
        guardar_equipos(equipos)
        print(f"Equipo '{nombre_equipo}' creado correctamente.")

def alta_jugador(nombre_equipo, nombre_jugador):
    equipos = cargar_equipos()
    if nombre_equipo not in equipos:
        print(f"El equipo '{nombre_equipo}' no existe.")
        return

    jugadores = equipos[nombre_equipo]["jugadores"]

    # Comprobar duplicado
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre_jugador.lower():
            print(f"El jugador '{nombre_jugador}' ya está registrado en '{nombre_equipo}'.")
            return

    jugadores.append({"nombre": nombre_jugador, "goles": 0})
    guardar_equipos(equipos)
    print(f"Jugador '{nombre_jugador}' dado de alta en el equipo '{nombre_equipo}'.")

def listar_jugadores(nombre_equipo):
    equipos = cargar_equipos()
    if nombre_equipo not in equipos:
        print(f"El equipo '{nombre_equipo}' no existe.")
        return

    jugadores = equipos[nombre_equipo]["jugadores"]
    if not jugadores:
        print(f"No hay jugadores en el equipo '{nombre_equipo}'.")
        return

    print(f"Jugadores del equipo '{nombre_equipo}':")
    for jugador in jugadores:
        print(f"- {jugador['nombre']} (Goles: {jugador['goles']})")

# ---------------------------
# Función interactiva principal
# ---------------------------
def menu_alta_jugadores():
    print("=== Gestión de Altas de Jugadores ===")
    nombre_equipo = input("Introduce el nombre del equipo: ").strip()
    alta_equipo(nombre_equipo)

    while True:
        accion = input("\n¿Qué quieres hacer? (1=Agregar jugador, 2=Listar jugadores, 3=Salir): ").strip()
        if accion == "1":
            while True:
                nombre_jugador = input("Nombre del jugador a dar de alta (ENTER para salir): ").strip()
                if not nombre_jugador:  # ENTER vacío = salir del subbucle
                    break
                alta_jugador(nombre_equipo, nombre_jugador)
        elif accion == "2":
            listar_jugadores(nombre_equipo)
        elif accion == "3":
            print("Saliendo del gestor de jugadores.")
            break
        else:
            print("Opción no válida. Elige 1, 2 o 3.")

