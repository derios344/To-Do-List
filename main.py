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

def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
        return

    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea['nombre']} - {'Completada' if tarea['completada'] else 'Pendiente'}")

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

        tarea = {"nombre": nombre,"completada": False}

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
                nueva_tarea = input("Introduzca el nuevo nombre de la tarea: ").strip()
                if nueva_tarea == "":
                    print("El nombre de la tarea no puede estar vacío. Inténtelo de nuevo.")
                    continue
                tareas[indice]["nombre"] = nueva_tarea
                guardar_tareas()
                print(f"Tarea actualizada a '{nueva_tarea}'.")
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

cargar_tareas()

while True:
    print("\nOpciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Editar tarea")
    print("5. Marcar tarea como completada")
    print("6. Salir")

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
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
