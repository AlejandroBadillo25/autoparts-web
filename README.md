# autoparts-web

Proyecto desarrollado en Python y Django para administrar la web de una refaccionaria. El sistema permite gestionar categorías, subcategorías y productos de autopartes con funcionalidades completas de creación, listado y búsqueda.

## **Descripción**

Este proyecto incluye:
- Herencia de templates para mantener una estructura consistente
- Formularios de creación para categorías, subcategorías y productos
- Sistema de búsqueda en tiempo real con filtrado
- Panel de administración de Django
- Interfaz responsive con Bootstrap 5
- Base de datos SQLite

## **Tecnologías utilizadas**

- Python 3.11
- Django
- Bootstrap 5
- SQLite

## **Estructura de datos**

El proyecto cuenta con tres modelos principales:

**Category (Categorías)**: Permite organizar los productos en categorías principales (ej. Motor, Frenos, Suspensión).

**Subcategory (Subcategorías)**: Clasificaciones más específicas dentro de cada categoría.

**Products (Productos)**: Información completa de autopartes incluyendo nombre, descripción, precio, stock y relación con categoría y subcategoría.

## **Características principales**

- Listado completo de categorías, subcategorías y productos
- Creación de nuevos registros mediante formularios validados
- Búsqueda por nombre con filtrado instantáneo
- Interfaz intuitiva y responsive
- Panel de administración para gestión avanzada

## **Requisitos previos**

- Python 3.11 o superior instalado
- Git instalado

## **Pasos para utilizar el proyecto**

**1. Clonar el repositorio de Github**

```bash
git clone https://github.com/AlejandroBadillo25/autoparts-web.git
cd autoparts-web
```

**2. Crear un entorno virtual**

En **macOS/Linux**:
```bash
python -m venv .venv
```

En **Windows**:
```bash
python -m venv .venv
```

**3. Activar el entorno virtual**

En **macOS/Linux**:
```bash
source .venv/bin/activate
```

En **Windows (CMD)**:
```bash
.venv\Scripts\activate.bat
```

En **Windows (PowerShell)**:
```bash
.venv\Scripts\Activate.ps1
```

**4. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**5. Ejecutar las migraciones**

```bash
python manage.py migrate
```

**6. Crear un superusuario (opcional, para acceder al panel de administración)**

```bash
python manage.py createsuperuser
```

**7. Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

**8. Acceder a la aplicación**

Abrir el navegador en: `http://127.0.0.1:8000/`

Panel de administración: `http://127.0.0.1:8000/admin/`

## **Rutas principales**

- `/` - Página de inicio con listado de productos
- `/category/` - Listado de categorías
- `/category/create/` - Crear nueva categoría
- `/subcategory/` - Listado de subcategorías
- `/subcategory/create/` - Crear nueva subcategoría
- `/products/` - Listado de productos
- `/products/create/` - Crear nuevo producto

