from datetime import datetime

from .models import Tarea
from .storage import ArchivoTareas


class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.persistencia = ArchivoTareas(archivo)
        self.tareas = self.persistencia.cargar()

    def cargar_tareas(self):
        self.tareas = self.persistencia.cargar()

    def guardar_tareas(self):
        self.persistencia.guardar(self.tareas)

    def validar_fecha(self, fecha_texto):
        try:
            fecha_obj = datetime.strptime(fecha_texto, "%d-%m-%Y").date()
            fecha_hoy = datetime.now().date()
            if fecha_obj < fecha_hoy:
                return False, "La fecha no puede ser del pasado."
            return True, ""
        except ValueError:
            return False, "Formato inválido. Use DD-MM-YYYY"

    def obtener_tareas(self):
        return list(self.tareas)

    def agregar_tarea(self, nombre, prioridad, descripcion="", fecha_limite=""):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("Introduzca un nombre válido.")

        duplicado = any(tarea.nombre.lower() == nombre.lower() for tarea in self.tareas)
        if duplicado:
            raise ValueError("Esta tarea ya existe en la lista.")

        tarea = Tarea(
            nombre=nombre,
            completada=False,
            prioridad=prioridad,
            descripcion=descripcion.strip(),
            fecha_limite=fecha_limite,
        )
        self.tareas.append(tarea)
        self.guardar_tareas()
        return tarea

    def eliminar_tarea(self, indice):
        tarea = self.tareas.pop(indice)
        self.guardar_tareas()
        return tarea

    def editar_tarea(self, indice, nombre=None, prioridad=None, descripcion=None, fecha_limite=None):
        tarea = self.tareas[indice]

        if nombre is not None:
            tarea.nombre = nombre.strip()

        if prioridad is not None:
            tarea.prioridad = prioridad

        if descripcion is not None:
            tarea.descripcion = descripcion.strip()

        if fecha_limite is not None:
            tarea.fecha_limite = fecha_limite

        self.guardar_tareas()
        return tarea

    def marcar_como_completada(self, indice):
        tarea = self.tareas[indice]
        tarea.completada = True
        self.guardar_tareas()
        return tarea

    def tareas_ordenadas_por_prioridad(self):
        return sorted(self.tareas, key=lambda tarea: (tarea.prioridad, tarea.completada))

    def tareas_ordenadas_por_fecha(self):
        tareas_con_fecha = [tarea for tarea in self.tareas if tarea.fecha_limite.strip()]
        tareas_sin_fecha = [tarea for tarea in self.tareas if not tarea.fecha_limite.strip()]

        tareas_con_fecha.sort(key=lambda tarea: datetime.strptime(tarea.fecha_limite, "%d-%m-%Y"))
        return tareas_con_fecha, tareas_sin_fecha
