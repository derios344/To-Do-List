# Gestor de tareas

Aplicación de consola desarrollada en Python para administrar una lista de tareas.

El programa permite crear, modificar, eliminar y organizar tareas, guardando la información de forma persistente mediante archivos JSON.

## Características

- Crear tareas.
- Mostrar todas las tareas.
- Editar tareas existentes.
- Eliminar tareas.
- Marcar tareas como completadas.
- Sistema de prioridades.
- Mostrar tareas por prioridad.
- Agregar descripciones detalladas a las tareas.
- Editar descripciones de tareas.
- Visualización mejorada de descripciones largas.
- Agregar fechas límite a las tareas.
- Validación de fechas (no permite fechas del pasado).
- Mostrar tareas ordenadas por fecha límite más cercana.
- Editar fechas límite de tareas existentes.
- Evitar tareas duplicadas.
- Guardado automático de datos.
- Carga de datos al iniciar el programa.
- Validación de entradas del usuario.

## Tecnologías utilizadas

- Python 3.
- JSON para almacenamiento de datos.
- Librería `datetime` para manejo de fechas y validación.

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
- **nombre**: El título de la tarea.
- **prioridad**: 1=Alta, 2=Media, 3=Baja.
- **completada**: true si está hecha, false si está pendiente.
- **descripcion**: Detalles adicionales (opcional).
- **fecha_limite**: Fecha de vencimiento en formato DD-MM-YYYY (opcional).

## Instalación

Clonar el repositorio:

```bash
ggit clone https://github.com/derios344/To-Do-List.git
```

Entrar en la carpeta del proyecto:

```bash
cd To-Do-List
```

## Ejecutar el programa

```bash
python main.py
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
```
Introduzca el nombre de la tarea: Comprar pan
Prioridad (1-3) [2]: 1
Introduzca una descripción (opcional): Pan integral para el desayuno
Introduzca fecha límite (DD-MM-YYYY) o dejar vacío: 25-07-2026
```

La fecha límite:
- Es **opcional** (puedes dejar vacío presionando Enter)
- Debe estar en formato **DD-MM-YYYY** (ejemplo: 25-07-2026)
- **No puede ser del pasado** (el programa valida automáticamente)

Las tareas se guardan automáticamente en el archivo:

```text
tareas.json
```

por lo que los datos permanecen aunque el programa se cierre.

## Próximas mejoras

- Separar el proyecto en múltiples módulos.
- Implementar programación orientada a objetos.
- Migrar almacenamiento de JSON a SQLite.
- Crear una interfaz gráfica.

## Autor

D3R1OS

Proyecto realizado como práctica de aprendizaje de Python y desarrollo de software.