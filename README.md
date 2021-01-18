# ALUMNUSB-SYSTEM
Web application using gamification strategies for the AlumnUSB NGO. It seeks to motivate graduates of the Simón Bolívar University to make donations constantly through a medal system. In addition, the application allows you to view user statistics

#
Software and versions
---------

- Python: 3.6.12
- PIP: 20.3.3
- Postgres: 13.1
- Docker: 19.03.8

#
Requirements to run
---------

- Python (>=3.x <3.8.x)

#
Instrucciones
---------

- On the root file where 'Dockerfile' file is, run the following command
```
$ docker-compose up
```
- Finally check if the server is running on the docker cotainer by directing http://localhost:8000/ in your browser

- NOTE: If you need to erase the data on the database erase the postgres container with the following command 
```
$ docker container rm alumnusb-system_db_1
```