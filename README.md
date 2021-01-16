# ALUMNUSB-SYSTEM
Sistema para AlumnUSB. Continuación para la materia de Sistemas 2

#
Herramientas y versiones:
---------

- Python: 3.6.12
- PIP: 20.3.3
- Postgres: 13.1

#
Requisitos para ejecutar:
---------

- Python (>=3.x <3.8.x)
#
Instrucciones:
---------

- Clonar el repo
- Crear y activar ambiente virtual (virtualenv)
- Instalar dependencias:
```
$ pip install -r requirements.txt
```
- Ejecutar script para inicializar la BD
```
$ bash createlocaldb.sh
```
- Correr las migraciones ya existentes
```
$ python manage.py migrate
```
- Ejecutar el servidor en desarrollo
```
$ python manage.py runserver
```
- Ingresar en el navegador a http://localhost:8000/
