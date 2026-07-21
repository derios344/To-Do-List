from app.console import Consola
from app.services import GestorTareas


if __name__ == "__main__":
    gestor = GestorTareas("tareas.db")
    consola = Consola(gestor)
    consola.ejecutar()

