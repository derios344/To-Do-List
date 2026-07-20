"""
Sistema de lista de tareas

Autor: D3R1OS

Descripción:
Programa de gestión de una lista de tareas en consola
Permite agregar, eliminar, editar y mostrar tareas
Los datos se almacenan de forma permanente en un archivo JSON

"""

import json
from datetime import datetime

PRIORIDAD_LABEL = {1: "Alta", 2: "Media", 3: "Baja"}


class Tarea:
    def __init__(self, nombre, completada=False, prioridad=2, descripcion="", fecha_limite=""):
        self.nombre = nombre
        self.completada = completada
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            nombre=datos.get("nombre", ""),
            completada=datos.get("completada", False),
            prioridad=datos.get("prioridad", 2),
            descripcion=datos.get("descripcion", ""),
            fecha_limite=datos.get("fecha_limite", ""),
        )

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "completada": self.completada,
            "prioridad": self.prioridad,
            "descripcion": self.descripcion,
            "fecha_limite": self.fecha_limite,
        }

    @property
    def estado(self):
        return "Completada" if self.completada else "Pendiente"

    @property
    def prioridad_label(self):
        return PRIORIDAD_LABEL.get(self.prioridad, "Media")


class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = []

    def cargar_tareas(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            self.tareas = []
            return

        self.tareas = []
        for dato in datos:
            tarea = Tarea.desde_diccionario(dato)
            self.tareas.append(tarea)

    def guardar_tareas(self):
        datos = [tarea.to_dict() for tarea in self.tareas]
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def validar_fecha(self, fecha_texto):
        try:
            fecha_obj = datetime.strptime(fecha_texto, "%d-%m-%Y").date()
            fecha_hoy = datetime.now().date()
            if fecha_obj < fecha_hoy:
                return False, "La fecha no puede ser del pasado."
            return True, ""
        except ValueError:
            return False, "Formato inválido. Use DD-MM-YYYY"

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return

        print("\nLista de Tareas:")
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")

            fecha_limite = tarea.fecha_limite.strip()
            if fecha_limite:
                print(f"    Fecha límite: {fecha_limite}")

            descripcion = tarea.descripcion.strip()
            if descripcion:
                print("    " + "-" * 50)
                print(f"    Descripción: {descripcion}")
                print("    " + "-" * 50)

            print()

    def agregar_tarea(self):
        while True:
            nombre = input("Introduzca el nombre de la tarea: ").strip()
            print()

            if nombre == "":
                print("Introduzca un nombre válido.")
                continue

            duplicado = any(tarea.nombre.lower() == nombre.lower() for tarea in self.tareas)
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

            fecha_limite = ""
            while True:
                fecha_input = input("Introduzca fecha límite (DD-MM-YYYY) o dejar vacío: ").strip()
                if fecha_input == "":
                    break
                valida, mensaje = self.validar_fecha(fecha_input)
                if valida:
                    fecha_limite = fecha_input
                    break
                else:
                    print(mensaje)

            tarea = Tarea(
                nombre=nombre,
                completada=False,
                prioridad=prioridad,
                descripcion=descripcion,
                fecha_limite=fecha_limite,
            )

            self.tareas.append(tarea)
            self.guardar_tareas()
            print(f"Tarea '{nombre}' agregada correctamente.")

            seguir = input("¿Desea agregar otra tarea? (s/n): ").strip().lower()
            if seguir != "s":
                break

    def eliminar_tarea(self):
        if not self.tareas:
            print("No hay tareas para eliminar.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea eliminar: ")) - 1
                if 0 <= indice < len(self.tareas):
                    tarea_eliminada = self.tareas.pop(indice)
                    self.guardar_tareas()
                    print(f"Tarea '{tarea_eliminada.nombre}' eliminada correctamente.")
                    break
                else:
                    print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def editar_tarea(self):
        if not self.tareas:
            print("No hay tareas para editar.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea editar: ")) - 1
                if 0 <= indice < len(self.tareas):
                    tarea = self.tareas[indice]

                    nueva_tarea = input("Introduzca el nuevo nombre de la tarea (enter para no cambiar): ").strip()
                    if nueva_tarea != "":
                        tarea.nombre = nueva_tarea

                    while True:
                        prioridad_input = input(
                            f"Prioridad actual {tarea.prioridad_label}. Nueva prioridad 1=Alta,2=Media,3=Baja (enter para no cambiar): "
                        ).strip()
                        if prioridad_input == "":
                            break
                        try:
                            prioridad_val = int(prioridad_input)
                            if prioridad_val not in (1, 2, 3):
                                print("Prioridad inválida. Elija 1, 2 o 3.")
                                continue
                            tarea.prioridad = prioridad_val
                            break
                        except ValueError:
                            print("Por favor, introduzca un número válido para la prioridad.")

                    descripcion_input = input(
                        f"Descripción actual: {tarea.descripcion}\nNueva descripción (enter para no cambiar): "
                    ).strip()
                    if descripcion_input != "":
                        tarea.descripcion = descripcion_input

                    while True:
                        fecha_actual = tarea.fecha_limite
                        fecha_input = input(
                            f"Fecha límite actual: {fecha_actual}\nNueva fecha (DD-MM-YYYY) o dejar vacío (enter para no cambiar): "
                        ).strip()
                        if fecha_input == "":
                            break
                        valida, mensaje = self.validar_fecha(fecha_input)
                        if valida:
                            tarea.fecha_limite = fecha_input
                            break
                        else:
                            print(mensaje)

                    self.guardar_tareas()
                    print(f"Tarea actualizada a '{tarea.nombre}'.")
                    break
                else:
                    print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def marcar_como_completada(self):
        if not self.tareas:
            print("No hay tareas para marcar como completadas.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea marcar como completada: ")) - 1
                if 0 <= indice < len(self.tareas):
                    self.tareas[indice].completada = True
                    self.guardar_tareas()
                    print(f"Tarea '{self.tareas[indice].nombre}' marcada como completada.")
                    break
                else:
                    print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def mostrar_tareas_ordenadas_por_prioridad(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return

        tareas_ordenadas = sorted(self.tareas, key=lambda t: (t.prioridad, t.completada))
        print("\nLista de Tareas (ordenadas por prioridad):")
        for i, tarea in enumerate(tareas_ordenadas, start=1):
            print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")

            fecha_limite = tarea.fecha_limite.strip()
            if fecha_limite:
                print(f"    Fecha límite: {fecha_limite}")

            descripcion = tarea.descripcion.strip()
            if descripcion:
                print("    " + "-" * 50)
                print(f"    Descripción: {descripcion}")
                print("    " + "-" * 50)

            print()

    def mostrar_tareas_por_fecha(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return

        tareas_con_fecha = []
        tareas_sin_fecha = []

        for tarea in self.tareas:
            if tarea.fecha_limite.strip():
                tareas_con_fecha.append(tarea)
            else:
                tareas_sin_fecha.append(tarea)

        tareas_con_fecha.sort(key=lambda t: datetime.strptime(t.fecha_limite, "%d-%m-%Y"))

        print("\nLista de Tareas (ordenadas por fecha límite más cercana):")

        for i, tarea in enumerate(tareas_con_fecha, start=1):
            print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")
            print(f"    Fecha límite: {tarea.fecha_limite}")

            descripcion = tarea.descripcion.strip()
            if descripcion:
                print("    " + "-" * 50)
                print(f"    Descripción: {descripcion}")
                print("    " + "-" * 50)

            print()

        if tareas_sin_fecha:
            print("Tareas sin fecha límite:")
            for i, tarea in enumerate(tareas_sin_fecha, start=1):
                print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")

                descripcion = tarea.descripcion.strip()
                if descripcion:
                    print("    " + "-" * 50)
                    print(f"    Descripción: {descripcion}")
                    print("    " + "-" * 50)

                print()

    def ejecutar(self):
        self.cargar_tareas()

        while True:
            print("\nOpciones:")
            print("1. Mostrar tareas")
            print("2. Agregar tarea")
            print("3. Eliminar tarea")
            print("4. Editar tarea")
            print("5. Marcar tarea como completada")
            print("6. Mostrar tareas ordenadas por prioridad")
            print("7. Mostrar tareas ordenadas por fecha límite")
            print("8. Salir")

            opcion = input("Seleccione una opción (1-8): ").strip()

            if opcion == "1":
                self.mostrar_tareas()
            elif opcion == "2":
                self.agregar_tarea()
            elif opcion == "3":
                self.eliminar_tarea()
            elif opcion == "4":
                self.editar_tarea()
            elif opcion == "5":
                self.marcar_como_completada()
            elif opcion == "6":
                self.mostrar_tareas_ordenadas_por_prioridad()
            elif opcion == "7":
                self.mostrar_tareas_por_fecha()
            elif opcion == "8":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")


if __name__ == "__main__":
    gestor = GestorTareas()
    gestor.ejecutar()
