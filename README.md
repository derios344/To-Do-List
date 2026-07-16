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
- Evitar tareas duplicadas.
- Guardado automático de datos.
- Carga de datos al iniciar el programa.
- Validación de entradas del usuario.

## Tecnologías utilizadas

- Python 3.
- JSON para almacenamiento de datos.

## Estructura de una tarea

Cada tarea se almacena con la siguiente información:

```json
{
    "nombre": "Estudiar Python",
    "prioridad": "Alta",
    "completada": false
}
```

## Instalación

Clonar el repositorio:

```bash
git clone git@github.com:derios344/To-Do-List.git
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
6. Salir
```

Las tareas se guardan automáticamente en el archivo:

```text
tareas.json
```

por lo que los datos permanecen aunque el programa se cierre.

## Próximas mejoras

- Agregar descripción a las tareas.
- Agregar fechas límite.
- Crear filtros de búsqueda.
- Ordenar tareas por prioridad.
- Separar el proyecto en múltiples módulos.
- Implementar programación orientada a objetos.
- Migrar almacenamiento de JSON a SQLite.
- Crear una interfaz gráfica.

## Autor

D3R1OS

Proyecto realizado como práctica de aprendizaje de Python y desarrollo de software.