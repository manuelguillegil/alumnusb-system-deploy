# ALUMNUSB-SYSTEM
Web application using gamification strategies for the AlumnUSB NGO. It seeks to motivate graduates of the Simón Bolívar University to make donations constantly through a medal system. In addition, the application allows you to view user statistics

#
Software and versions
---------

- Python: 3.6.12
- PIP: 20.3.3
- Postgres: 13.1

#
Requirements to run
---------

- Python (>=3.x <3.8.x)
#
Instructions
---------

- Clone the repo
- Create and activate virtual enviroment (virtualenv)
- Install dependencies
```
$ pip install -r requirements.txt
```
- Execute script to initialize DB
```
$ bash createlocaldb.sh
```
- Run migrations that already exists
```
$ python manage.py migrate
```
- Run the development server
```
$ python manage.py runserver
```
- Into to the browser in http://localhost:8000/
