"""
Sistema de lista de tareas

Autor: D3R1OS

Descripción:
Programa de gestión de una lista de tareas en consola
Permite agregar, eliminar, editar y mostrar tareas
Los datos se almacenan de forma permanente en un archivo JSON

"""

import json

tareas = []

PRIORIDAD_LABEL = {1: "Alta", 2: "Media", 3: "Baja"}

def guardar_tareas():
    with open("tareas.json", "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r", encoding="utf-8") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []
    for tarea in tareas:
        if "prioridad" not in tarea:
            tarea["prioridad"] = 2
        if "descripcion" not in tarea:
            tarea["descripcion"] = ""

def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
        return

    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        prioridad_label = PRIORIDAD_LABEL.get(tarea.get("prioridad", 2), "Media")
        print(f"{i}. {tarea['nombre']} - {estado} - Prioridad: {prioridad_label}")
        descripcion = tarea.get("descripcion", "").strip()
        if descripcion:
            print(f"    Descripción: {descripcion}")

def agregar_tarea():
    while True:
        nombre = input("Introduzca el nombre de la tarea: ").strip()
        print()

        if nombre == "":
            print("Introduzca un nombre válido.")
            continue

        duplicado = any(
            tarea["nombre"].lower() == nombre.lower() 
            for tarea in tareas
        )

        if duplicado:
            print("Esta tarea ya existe en la lista. Inténtelo de nuevo.")
            continue

        
        while True:
            print("Seleccione prioridad: 1=Alta, 2=Media, 3=Baja")
            try:
                prioridad = int(input("Prioridad (1-3) [2]: ").strip() or 2)
                if prioridad not in (1, 2, 3):
                    print("Prioridad inválida. Elija 1, 2 o 3.")
                    continue
                break
            except ValueError:
                print("Por favor, introduzca un número válido para la prioridad.")

        descripcion = input("Introduzca una descripción (opcional): ").strip()

        tarea = {"nombre": nombre, "completada": False, "prioridad": prioridad, "descripcion": descripcion}

        tareas.append(tarea)
        guardar_tareas()
        print(f"Tarea '{nombre}' agregada correctamente.")
        
        seguir = input("¿Desea agregar otra tarea? (s/n): ").strip().lower() 
        if seguir != "s":
            break

def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        return

    mostrar_tareas()
    while True:
        try:
            indice = int(input("Introduzca el número de la tarea que desea eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                guardar_tareas()
                print(f"Tarea '{tarea_eliminada['nombre']}' eliminada correctamente.")
                break
            else:
                print("Número de tarea inválido. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, introduzca un número válido.")

def editar_tarea():
    if not tareas:
        print("No hay tareas para editar.")
        return

    mostrar_tareas()
    while True:
        try:
            indice = int(input("Introduzca el número de la tarea que desea editar: ")) - 1
            if 0 <= indice < len(tareas):
                nueva_tarea = input("Introduzca el nuevo nombre de la tarea (enter para no cambiar): ").strip()
                if nueva_tarea != "":
                    tareas[indice]["nombre"] = nueva_tarea

                # Editar prioridad
                while True:
                    prioridad_input = input(f"Prioridad actual {PRIORIDAD_LABEL.get(tareas[indice].get('prioridad',2))}. Nueva prioridad 1=Alta,2=Media,3=Baja (enter para no cambiar): ").strip()
                    if prioridad_input == "":
                        break
                    try:
                        prioridad_val = int(prioridad_input)
                        if prioridad_val not in (1,2,3):
                            print("Prioridad inválida. Elija 1, 2 o 3.")
                            continue
                        tareas[indice]["prioridad"] = prioridad_val
                        break
                    except ValueError:
                        print("Por favor, introduzca un número válido para la prioridad.")

                # Editar descripción
                descripcion_input = input(f"Descripción actual: {tareas[indice].get('descripcion','')}\nNueva descripción (enter para no cambiar): ").strip()
                if descripcion_input != "":
                    tareas[indice]["descripcion"] = descripcion_input

                guardar_tareas()
                print(f"Tarea actualizada a '{tareas[indice]['nombre']}'.")
                break
            else:
                print("Número de tarea inválido. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, introduzca un número válido.")
        

def marcar_como_completada():
    if not tareas:
        print("No hay tareas para marcar como completadas.")
        return

    mostrar_tareas()
    while True:
        try:
            indice = int(input("Introduzca el número de la tarea que desea marcar como completada: ")) - 1
            if 0 <= indice < len(tareas):
                tareas[indice]["completada"] = True
                guardar_tareas()
                print(f"Tarea '{tareas[indice]['nombre']}' marcada como completada.")
                break
            else:
                print("Número de tarea inválido. Inténtelo de nuevo.")
        except ValueError:
            print("Por favor, introduzca un número válido.")

def mostrar_tareas_ordenadas_por_prioridad():
    if not tareas:
        print("No hay tareas en la lista.")
        return

    # Ordenar por prioridad ascendente (1=Alta) y luego por completada
    tareas_ordenadas = sorted(tareas, key=lambda t: (t.get('prioridad', 2), t.get('completada', False)))
    print("\nLista de Tareas (ordenadas por prioridad):")
    for i, tarea in enumerate(tareas_ordenadas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        prioridad_label = PRIORIDAD_LABEL.get(tarea.get("prioridad", 2), "Media")
        print(f"{i}. {tarea['nombre']} - {estado} - Prioridad: {prioridad_label}")

cargar_tareas()

while True:
    print("\nOpciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Editar tarea")
    print("5. Marcar tarea como completada")
    print("6. Mostrar tareas ordenadas por prioridad")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-6): ").strip()

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        editar_tarea()
    elif opcion == "5":
        marcar_como_completada()
    elif opcion == "6":
        mostrar_tareas_ordenadas_por_prioridad()
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
