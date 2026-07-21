import json
import sqlite3
from pathlib import Path

from .models import Tarea


class ArchivoTareas:
    def __init__(self, archivo="tareas.db"):
        self.archivo = Path(archivo)
        self.db_path = self.archivo.with_suffix(".db") if self.archivo.suffix.lower() == ".json" else self.archivo
        self._inicializar_bd()

    def _inicializar_bd(self):
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(self.db_path) as conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS tareas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    completada INTEGER NOT NULL DEFAULT 0,
                    prioridad INTEGER NOT NULL DEFAULT 2,
                    descripcion TEXT NOT NULL DEFAULT '',
                    fecha_limite TEXT NOT NULL DEFAULT ''
                )
                """
            )
            conexion.commit()

        if not self._hay_datos() and self.archivo.exists() and self.archivo.suffix.lower() == ".json":
            self._migrar_json_a_sqlite()

    def _hay_datos(self):
        with sqlite3.connect(self.db_path) as conexion:
            resultado = conexion.execute("SELECT COUNT(*) FROM tareas").fetchone()
        return resultado[0] > 0

    def _migrar_json_a_sqlite(self):
        try:
            datos = json.loads(self.archivo.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return

        with sqlite3.connect(self.db_path) as conexion:
            for tarea_data in datos:
                conexion.execute(
                    """
                    INSERT INTO tareas (nombre, completada, prioridad, descripcion, fecha_limite)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        tarea_data.get("nombre", ""),
                        1 if tarea_data.get("completada", False) else 0,
                        tarea_data.get("prioridad", 2),
                        tarea_data.get("descripcion", ""),
                        tarea_data.get("fecha_limite", ""),
                    ),
                )
            conexion.commit()

    def cargar(self):
        with sqlite3.connect(self.db_path) as conexion:
            filas = conexion.execute(
                """
                SELECT nombre, completada, prioridad, descripcion, fecha_limite
                FROM tareas
                ORDER BY id
                """
            ).fetchall()

        return [
            Tarea(
                nombre=nombre,
                completada=bool(completada),
                prioridad=prioridad,
                descripcion=descripcion,
                fecha_limite=fecha_limite,
            )
            for nombre, completada, prioridad, descripcion, fecha_limite in filas
        ]

    def guardar(self, tareas):
        with sqlite3.connect(self.db_path) as conexion:
            conexion.execute("DELETE FROM tareas")
            for tarea in tareas:
                conexion.execute(
                    """
                    INSERT INTO tareas (nombre, completada, prioridad, descripcion, fecha_limite)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        tarea.nombre,
                        1 if tarea.completada else 0,
                        tarea.prioridad,
                        tarea.descripcion,
                        tarea.fecha_limite,
                    ),
                )
            conexion.commit()
