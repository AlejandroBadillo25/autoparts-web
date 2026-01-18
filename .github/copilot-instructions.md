# Instrucciones para GitHub Copilot

## Contexto del Proyecto
Este es un proyecto web de autopartes desarrollado con **Python** y **Django**.

## Stack Tecnológico
- **Lenguaje**: Python 3.x
- **Framework**: Django
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: HTML, CSS (Bootstrap si está disponible)

## Estructura del Proyecto
- `autoparts/`: Configuración principal de Django (settings, urls, wsgi)
- `autopartsApp/`: Aplicación principal con modelos, vistas, formularios y templates
- `templates/autopartsApp/`: Templates HTML de la aplicación

## Modelos Principales
- Category (Categorías de productos)
- Subcategory (Subcategorías de productos)
- Products (Productos de autopartes)

## Convenciones de Código
- Usar nombres en inglés para clases, funciones y variables
- Seguir PEP 8 para estilo de código Python
- Usar Django class-based views cuando sea apropiado
- Mantener la separación de responsabilidades entre models, views y forms

## Funcionalidades
- CRUD de categorías, subcategorías y productos
- Sistema de autenticación de usuarios (login, registro, logout)
- Interfaz responsive con templates HTML

## Al escribir código
- Usar Django ORM para consultas a la base de datos
- Implementar validaciones en forms.py
- Usar decoradores de Django para protección de vistas (@login_required, etc.)
- Seguir el patrón MTV (Model-Template-View) de Django
- Incluir mensajes de feedback para el usuario (django.contrib.messages)
- Manejar errores apropiadamente con try-except cuando sea necesario

## Prioridades
1. Seguridad (validación de datos, protección CSRF, autenticación)
2. Código limpio y mantenible
3. Experiencia de usuario
4. Performance y optimización de queries
