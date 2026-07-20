from dataclasses import dataclass

PRIORIDAD_LABEL = {1: "Alta", 2: "Media", 3: "Baja"}


@dataclass
class Tarea:
    nombre: str
    completada: bool = False
    prioridad: int = 2
    descripcion: str = ""
    fecha_limite: str = ""

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
