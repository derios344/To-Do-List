import json
from pathlib import Path

from .models import Tarea


class ArchivoTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = Path(archivo)

    def cargar(self):
        if not self.archivo.exists():
            return []

        try:
            datos = json.loads(self.archivo.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

        return [Tarea.desde_diccionario(tarea) for tarea in datos]

    def guardar(self, tareas):
        datos = [tarea.to_dict() for tarea in tareas]
        self.archivo.write_text(
            json.dumps(datos, indent=4, ensure_ascii=False),
            encoding="utf-8",
        )
