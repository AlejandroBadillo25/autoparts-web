# 818 Autopartes - Sistema de Gestión Web

Sistema web desarrollado con Python y Django para la administración integral de una tienda de autopartes. Implementa arquitectura basada en Class-Based Views (CBV), herencia de templates y gestión de medios con funcionalidades completas de autenticación, autorización y administración de contenido.

## Descripción

Plataforma web completa para la gestión de inventario de autopartes que incluye:
- Sistema de autenticación y perfiles de usuario
- Gestión de categorías, subcategorías y productos con imágenes
- Sistema de banners y publicidad segmentado por sección
- Navegación jerárquica (categorías → subcategorías → productos)
- Búsqueda y filtrado en tiempo real
- Panel administrativo con control de permisos
- Interfaz responsive con Bootstrap 5
- Arquitectura basada en Class-Based Views

## Tecnologías Utilizadas

### Backend
- Python 3.11
- Django 5.2.9
- Pillow (gestión de imágenes)
- SQLite (desarrollo)

### Frontend
- HTML5
- CSS3
- Bootstrap 5.3.8
- Bootstrap Icons 1.11.3
- JavaScript (ES6+)

## Arquitectura del Proyecto

### Aplicaciones Django

**autopartsApp**: Gestión del catálogo de productos
- Categorías, subcategorías y productos
- Class-Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView)
- Sistema de búsqueda y filtrado
- Navegación jerárquica

**accountsApp**: Autenticación y gestión de usuarios
- Login, registro y logout
- Perfiles de usuario con imagen
- Cambio de contraseña con AJAX
- Mixins de autenticación (LoginRequiredMixin)

**autopartsBannersApp**: Sistema de publicidad
- Gestión de banners por sección (inicio, categorías, subcategorías, productos)
- Segmentación por categoría/subcategoría específica
- Control de fechas de vigencia
- Permisos exclusivos para staff/superuser
- Mixin personalizado (StaffOrSuperuserRequiredMixin)

### Estructura de Modelos

**Category**
- Campos: name, description, image, created_at, updated_at
- Relación: OneToMany con Subcategory

**Subcategory**
- Campos: name, description, category (FK), image, created_at, updated_at
- Relación: ManyToOne con Category, OneToMany con Products

**Products**
- Campos: name, description, category (FK), subcategory (FK), price, stock, image, created_at, updated_at
- Relaciones: ManyToOne con Category y Subcategory

**UserProfile**
- Campos: user (OneToOne), phone, address, profile_image
- Extensión del modelo User de Django

**Banner**
- Campos: name, image, section, category (FK opcional), subcategory (FK opcional), start_date, end_date, is_active, order, created_by (FK)
- Validación de rangos de fechas
- Segmentación por sección y entidad específica

## Características Principales

### Gestión de Contenido
- CRUD completo para categorías, subcategorías y productos
- Carga y visualización de imágenes con placeholders
- Preview de imágenes antes de subir (FileReader API)
- Búsqueda en tiempo real con filtrado por nombre
- Navegación jerárquica mediante enlaces clickeables

### Sistema de Usuarios
- Autenticación completa (login, registro, logout)
- Perfiles personalizables con imagen
- Cambio de contraseña con validación AJAX
- Control de permisos basado en roles

### Sistema de Banners
- Gestión exclusiva para staff/superuser
- Segmentación por sección del sitio
- Asignación a categorías/subcategorías específicas
- Control de fechas de inicio y fin
- Activación/desactivación dinámica
- Orden de visualización personalizable

### Interfaz de Usuario
- Herencia de templates mediante base.html
- Componentes reutilizables (search_bar, create_button, empty_state)
- Responsive design con Bootstrap 5
- Mensajes de feedback (Django messages framework)
- Modales de confirmación para acciones destructivas
- Efectos hover y transiciones suaves

### Seguridad
- Protección CSRF en todos los formularios
- LoginRequiredMixin en vistas que requieren autenticación
- UserPassesTestMixin para validación de permisos personalizados
- Validación de formularios en cliente y servidor
- Control de acceso basado en autenticación para acciones CRUD

## Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/AlejandroBadillo25/autoparts-web.git
cd autoparts-web/autoparts-web
```

### 2. Crear y activar entorno virtual

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (CMD):**
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

### 7. Acceder a la aplicación

- Aplicación principal: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## Estructura de URLs

### autopartsApp

**Inicio:**
- `/` - Página principal con productos destacados

**Categorías:**
- `/category/` - Listado de categorías
- `/category/create/` - Crear categoría (requiere autenticación)
- `/category/<id>/` - Detalle de categoría con subcategorías
- `/category/<id>/edit/` - Editar categoría (requiere autenticación)
- `/category/<id>/delete/` - Eliminar categoría (requiere autenticación)

**Subcategorías:**
- `/subcategory/` - Listado de subcategorías
- `/subcategory/create/` - Crear subcategoría (requiere autenticación)
- `/subcategory/<id>/` - Detalle de subcategoría con productos y banners específicos
- `/subcategory/<id>/edit/` - Editar subcategoría (requiere autenticación)
- `/subcategory/<id>/delete/` - Eliminar subcategoría (requiere autenticación)

**Productos:**
- `/products/` - Listado de productos
- `/products/create/` - Crear producto (requiere autenticación)
- `/products/<id>/` - Detalle de producto
- `/products/<id>/edit/` - Editar producto (requiere autenticación)
- `/products/<id>/delete/` - Eliminar producto (requiere autenticación)

**Otros:**
- `/about/` - Página de contacto e información

### accountsApp

- `/accounts/login/` - Inicio de sesión
- `/accounts/register/` - Registro de usuarios
- `/accounts/logout/` - Cerrar sesión
- `/accounts/profile/edit/` - Editar perfil (requiere autenticación)
- `/accounts/profile/change-password/` - Cambiar contraseña (requiere autenticación)

### autopartsBannersApp

- `/banners/` - Listado de banners (requiere staff/superuser)
- `/banners/crear/` - Crear banner (requiere staff/superuser)
- `/banners/editar/<id>/` - Editar banner (requiere staff/superuser)
- `/banners/eliminar/<id>/` - Eliminar banner (requiere staff/superuser)
- `/banners/toggle/<id>/` - Activar/desactivar banner (requiere staff/superuser)

## Estructura de Archivos

```
autoparts-web/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── media/                          # Archivos subidos
│   ├── category_images/
│   ├── subcategory_images/
│   ├── product_images/
│   ├── banners/
│   └── profile_images/
├── autoparts/                      # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── autopartsApp/                   # App principal
│   ├── models.py
│   ├── views.py                    # Class-Based Views
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── autopartsApp/
│           ├── base.html           # Template base con herencia
│           ├── includes/           # Componentes reutilizables
│           │   ├── search_bar.html
│           │   ├── create_button.html
│           │   └── empty_state.html
│           ├── index.html
│           ├── category*.html
│           ├── subcategory*.html
│           ├── products*.html
│           └── about_me.html
├── accountsApp/                    # Autenticación
│   ├── models.py
│   ├── views.py                    # Class-Based Views
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── accountsApp/
│           ├── login.html
│           ├── register.html
│           └── profile_edit.html
└── autopartsBannersApp/            # Sistema de banners
    ├── models.py
    ├── views.py                    # Class-Based Views con Mixins
    ├── forms.py
    ├── urls.py
    ├── context_processors.py       # Banners globales
    └── templates/
        └── autopartsBannersApp/
            ├── banner_list.html
            ├── banner_form.html
            ├── banner_confirm_delete.html
            └── banner_display.html # Include reutilizable
```

## Patrones de Diseño Implementados

### Class-Based Views (CBV)
- **ListView**: Listados con búsqueda y filtrado
- **DetailView**: Vistas de detalle con contexto adicional
- **CreateView**: Formularios de creación con validación
- **UpdateView**: Formularios de edición
- **DeleteView**: Confirmación de eliminación
- **FormView**: Formularios personalizados (login, registro, perfil)
- **TemplateView**: Vistas estáticas (about_me)
- **View**: Vistas personalizadas (logout, toggle banner)

### Mixins de Django
- **LoginRequiredMixin**: Requiere autenticación
- **UserPassesTestMixin**: Validación de permisos personalizada
- **StaffOrSuperuserRequiredMixin**: Mixin personalizado para staff/superuser

### Template Inheritance
- Base template (base.html) con bloques extensibles
- Componentes reutilizables mediante {% include %}
- Context processors para datos globales (banners)

### DRY (Don't Repeat Yourself)
- Componentes reutilizables en templates/includes/
- Formularios ModelForm vinculados a modelos
- Mixins para lógica compartida entre vistas

## Funcionalidades Avanzadas

### Sistema de Context Processors
Los banners están disponibles globalmente mediante context processor:
- `banners_inicio`: Banners para la página principal
- `banners_categorias`: Banners para categorías
- `banners_subcategorias`: Banners para subcategorías
- `banners_productos`: Banners para productos

### Validaciones Personalizadas
- Rangos de fechas en banners (start_date <= end_date)
- Validación de imágenes (formatos permitidos)
- Validación de precios y stock positivos

### AJAX y JavaScript
- Cambio de contraseña con validación asíncrona
- Preview de imágenes antes de subir
- Modal de confirmación para eliminaciones

## Configuración de Medios

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Las imágenes se organizan automáticamente según el tipo:
- Categorías: `media/category_images/`
- Subcategorías: `media/subcategory_images/`
- Productos: `media/product_images/`
- Banners: `media/banners/`
- Perfiles: `media/profile_images/`

## Control de Permisos

### Visitantes (No autenticados)
- Ver categorías, subcategorías y productos
- Navegar jerárquicamente por el catálogo
- Ver banners públicos

### Usuarios Autenticados
- Todo lo anterior
- Crear, editar y eliminar categorías, subcategorías y productos
- Editar perfil personal
- Cambiar contraseña

### Staff/Superuser
- Todo lo anterior
- Gestionar banners
- Acceso al panel de administración de Django

## Desarrollo y Contribución

Este proyecto sigue las mejores prácticas de Django:
- Arquitectura basada en Class-Based Views
- Separación de responsabilidades (MTV pattern)
- Código limpio y documentado
- Validaciones en cliente y servidor
- Seguridad CSRF habilitada
- Gestión de archivos media
- Mensajes de feedback al usuario

## Autor

Alejandro Badillo Castilleja
- Email: kope_alex@hotmail.com
- LinkedIn: [www.linkedin.com/in/alejandro-badillo25](https://www.linkedin.com/in/alejandro-badillo25)
- GitHub: [github.com/AlejandroBadillo25](https://github.com/AlejandroBadillo25)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia correspondiente.

