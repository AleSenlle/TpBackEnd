# TpBackEnd
# Ramsey Review - App de Reseñas de Restaurantes

Este proyecto es una aplicación para reseñar restaurantes visitados y sus platos por los diferentes usuarios. 

## Roles de Usuarios

- **Reseñador**: Puede crear, leer, actualizar y eliminar reseñas de restaurantes.
- **Observador**: Puede leer reseñas de restaurantes.

## Niveles de Permisos

- **Staff**: Usuarios con permiso para la creación de nuevos restaurantes.
- **No Staff**: Usuarios sin permiso para crear restaurantes, pero pueden crear y/o leer reseñas.

## Funcionalidades

- **Reseñas de Restaurantes**: Los usuarios pueden escribir reseñas sobre los restaurantes que han visitado, así como sobre los platos que han probado.
- **Creación de Restaurantes**: Solo los usuarios con permisos de staff pueden añadir nuevos restaurantes a la plataforma.
- **Roles y Permisos**: Gestión de roles y permisos para asegurar que solo los usuarios autorizados pueden realizar ciertas acciones.

## Requisitos

- **Django**: Framework de desarrollo web utilizado.
- **PostgreSQL**: Base de datos utilizada.

## Configuración

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Configura la base de datos en el archivo `settings.py`.
4. Ejecuta las migraciones con `python manage.py migrate`.
5. Inicia el servidor con `python manage.py runserver`.

## Licencia

Este proyecto está bajo la licencia MIT.


