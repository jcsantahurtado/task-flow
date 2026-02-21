# TaskFlow

TaskFlow es una aplicación web desarrollada con Django para la gestión de proyectos y tareas.  
Forma parte de mi portafolio como desarrollador web y está enfocada en demostrar buenas prácticas, estructura limpia y manejo completo del flujo CRUD.

## Características

- Crear, editar y eliminar proyectos
- Crear, editar y eliminar tareas
- Relación entre proyectos y tareas
- Formularios con Django Forms / ModelForms
- Templates reutilizables
- Interfaz simple y clara
- Estructura profesional de proyecto Django

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite (desarrollo)

## Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/taskflow.git
cd taskflow
````

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en:
`http://127.0.0.1:8000/`

## Autor

Desarrollado por **Juan Santa**, con la turoria de FaztTech (https://www.youtube.com/@FaztTech)
Proyecto creado como parte de mi portafolio personal para demostrar habilidades en Django y desarrollo web.

## Notas

* La base de datos `db.sqlite3` no se incluye en el repositorio.
* Se genera automáticamente al ejecutar las migraciones.
* El proyecto está pensado para fines educativos y de portafolio.
