from .services import GestorTareas


class Consola:
    def __init__(self, gestor: GestorTareas):
        self.gestor = gestor

    def mostrar_tareas(self, tareas=None):
        tareas = tareas if tareas is not None else self.gestor.obtener_tareas()

        if not tareas:
            print("No hay tareas en la lista.")
            return

        print("\nLista de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")

            if tarea.fecha_limite.strip():
                print(f"    Fecha límite: {tarea.fecha_limite}")

            if tarea.descripcion.strip():
                print("    " + "-" * 50)
                print(f"    Descripción: {tarea.descripcion}")
                print("    " + "-" * 50)

            print()

    def pedir_prioridad(self):
        while True:
            print("Seleccione prioridad: 1=Alta, 2=Media, 3=Baja")
            try:
                prioridad = int(input("Prioridad (1-3) [2]: ").strip() or 2)
                if prioridad not in (1, 2, 3):
                    print("Prioridad inválida. Elija 1, 2 o 3.")
                    continue
                return prioridad
            except ValueError:
                print("Por favor, introduzca un número válido para la prioridad.")

    def pedir_fecha(self):
        while True:
            fecha_input = input("Introduzca fecha límite (DD-MM-YYYY) o dejar vacío: ").strip()
            if fecha_input == "":
                return ""

            valida, mensaje = self.gestor.validar_fecha(fecha_input)
            if valida:
                return fecha_input
            print(mensaje)

    def agregar_tarea(self):
        nombre = input("Introduzca el nombre de la tarea: ").strip()
        if not nombre:
            print("Introduzca un nombre válido.")
            return

        prioridad = self.pedir_prioridad()
        descripcion = input("Introduzca una descripción (opcional): ").strip()
        fecha_limite = self.pedir_fecha()

        try:
            tarea = self.gestor.agregar_tarea(nombre, prioridad, descripcion, fecha_limite)
            print(f"Tarea '{tarea.nombre}' agregada correctamente.")
        except ValueError as error:
            print(error)

    def eliminar_tarea(self):
        if not self.gestor.obtener_tareas():
            print("No hay tareas para eliminar.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea eliminar: ")) - 1
                if 0 <= indice < len(self.gestor.obtener_tareas()):
                    tarea_eliminada = self.gestor.eliminar_tarea(indice)
                    print(f"Tarea '{tarea_eliminada.nombre}' eliminada correctamente.")
                    break
                print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def editar_tarea(self):
        tareas = self.gestor.obtener_tareas()
        if not tareas:
            print("No hay tareas para editar.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea editar: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea = tareas[indice]

                    nuevo_nombre = input("Introduzca el nuevo nombre de la tarea (enter para no cambiar): ").strip()
                    if nuevo_nombre == "":
                        nuevo_nombre = None

                    prioridad = None
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
                            prioridad = prioridad_val
                            break
                        except ValueError:
                            print("Por favor, introduzca un número válido para la prioridad.")

                    descripcion = input(
                        f"Descripción actual: {tarea.descripcion}\nNueva descripción (enter para no cambiar): "
                    ).strip()
                    if descripcion == "":
                        descripcion = None
                    else:
                        descripcion = descripcion

                    fecha_limite = None
                    while True:
                        fecha_input = input(
                            f"Fecha límite actual: {tarea.fecha_limite}\nNueva fecha (DD-MM-YYYY) o dejar vacío (enter para no cambiar): "
                        ).strip()
                        if fecha_input == "":
                            break
                        valida, mensaje = self.gestor.validar_fecha(fecha_input)
                        if valida:
                            fecha_limite = fecha_input
                            break
                        print(mensaje)

                    self.gestor.editar_tarea(
                        indice,
                        nombre=nuevo_nombre,
                        prioridad=prioridad,
                        descripcion=descripcion,
                        fecha_limite=fecha_limite,
                    )
                    print(f"Tarea actualizada a '{tarea.nombre}'.")
                    break
                print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def marcar_como_completada(self):
        tareas = self.gestor.obtener_tareas()
        if not tareas:
            print("No hay tareas para marcar como completadas.")
            return

        self.mostrar_tareas()
        while True:
            try:
                indice = int(input("Introduzca el número de la tarea que desea marcar como completada: ")) - 1
                if 0 <= indice < len(tareas):
                    tarea = self.gestor.marcar_como_completada(indice)
                    print(f"Tarea '{tarea.nombre}' marcada como completada.")
                    break
                print("Número de tarea inválido. Inténtelo de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido.")

    def mostrar_tareas_ordenadas_por_prioridad(self):
        tareas_ordenadas = self.gestor.tareas_ordenadas_por_prioridad()
        self.mostrar_tareas(tareas_ordenadas)

    def mostrar_tareas_por_fecha(self):
        tareas_con_fecha, tareas_sin_fecha = self.gestor.tareas_ordenadas_por_fecha()

        if not tareas_con_fecha and not tareas_sin_fecha:
            print("No hay tareas en la lista.")
            return

        print("\nLista de Tareas (ordenadas por fecha límite más cercana):")
        for i, tarea in enumerate(tareas_con_fecha, start=1):
            print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")
            print(f"    Fecha límite: {tarea.fecha_limite}")
            print()

        if tareas_sin_fecha:
            print("Tareas sin fecha límite:")
            for i, tarea in enumerate(tareas_sin_fecha, start=1):
                print(f"{i}. {tarea.nombre} - {tarea.estado} - Prioridad: {tarea.prioridad_label}")
                print()

    def ejecutar(self):
        self.gestor.cargar_tareas()

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
