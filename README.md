# Gestor de tareas

Aplicación de consola desarrollada en Python para administrar una lista de tareas de forma simple y ordenada.

El programa permite crear, modificar, eliminar y organizar tareas, guardando la información de forma persistente en una base de datos SQLite.

## Características

- Crear tareas nuevas.
- Mostrar todas las tareas almacenadas.
- Editar tareas existentes.
- Eliminar tareas.
- Marcar tareas como completadas.
- Asignar prioridades (Alta, Media, Baja).
- Mostrar tareas ordenadas por prioridad.
- Agregar descripciones detalladas.
- Agregar fechas límite.
- Validar fechas para evitar fechas del pasado.
- Mostrar tareas ordenadas por fecha límite.
- Evitar tareas duplicadas.
- Guardado automático de datos.
- Carga automática de datos al iniciar el programa.
- Validación básica de entradas del usuario.

## Tecnologías utilizadas

- Python 3
- SQLite para almacenamiento persistente
- Librería datetime para manejo y validación de fechas

## Estructura del proyecto

El proyecto ahora está organizado de forma modular para que sea más claro y fácil de mantener:

- app/models.py: define la clase Tarea y sus propiedades.
- app/storage.py: gestiona la lectura y escritura de tareas en SQLite.
- app/services.py: contiene la lógica del gestor de tareas.
- app/console.py: maneja la interacción con el usuario en consola.
- main.py: es el punto de entrada del programa.

## Estructura de una tarea

Cada tarea se almacena con la siguiente información:

```json
{
    "nombre": "Estudiar Python",
    "prioridad": 1,
    "completada": false,
    "descripcion": "Estudiar capítulos 1-5 del curso online",
    "fecha_limite": "30-07-2026"
}
```

Donde:
- nombre: El título de la tarea.
- prioridad: 1=Alta, 2=Media, 3=Baja.
- completada: true si está hecha, false si está pendiente.
- descripcion: Detalles adicionales (opcional).
- fecha_limite: Fecha de vencimiento en formato DD-MM-YYYY (opcional).

## Instalación

Clona este repositorio o descárgalo en tu máquina y entra a la carpeta del proyecto:

```bash
git clone <url-del-repositorio>
cd To-Do-list
```

## Ejecutar el programa

```bash
python3 main.py
```

## Uso

Al iniciar el programa aparecerá un menú con las siguientes opciones:

```text
1. Mostrar tareas
2. Agregar tarea
3. Eliminar tarea
4. Editar tarea
5. Marcar tarea como completada
6. Mostrar tareas ordenadas por prioridad
7. Mostrar tareas ordenadas por fecha límite
8. Salir
```

### Agregar tarea con fecha límite

Cuando agregas una tarea, el programa te pide:

```text
Introduzca el nombre de la tarea: Comprar pan
Prioridad (1-3) [2]: 1
Introduzca una descripción (opcional): Pan integral para el desayuno
Introduzca fecha límite (DD-MM-YYYY) o dejar vacío: 25-07-2026
```

La fecha límite:
- Es opcional (puedes dejar vacío presionando Enter).
- Debe estar en formato DD-MM-YYYY.
- No puede ser del pasado.

Las tareas se guardan automáticamente en la base de datos:

```text
tareas.db
```

por lo que los datos permanecen aunque el programa se cierre.

## Próximas mejoras

- Crear una interfaz gráfica.
- Añadir más opciones de filtrado y búsqueda.
- Incorporar pruebas automatizadas.

## Autor

D3R1OS

Proyecto realizado como práctica de aprendizaje de Python y desarrollo de software.