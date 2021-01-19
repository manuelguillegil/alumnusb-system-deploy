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
Instructions
---------

<<<<<<< HEAD
- On the root foler where ``Dockerfile`` file is located, run the following command:
=======
- On the root file where 'Dockerfile' file is, run the following command.
>>>>>>> 1dacc6e88b802953a161f9f20c0ddb75c12112d2
```
$ docker-compose up
```
- Finally check if the server is running on the docker container by directing http://localhost:8000/ in your browser.

<<<<<<< HEAD
- **Note**: If you need to erase the data on the database delete the postgres container with the following command and compose after it: 
=======
- Note: If you need to erase the data on the database delete the postgres container with the following command and compose after it: 
>>>>>>> 1dacc6e88b802953a161f9f20c0ddb75c12112d2
```
$ docker container rm alumnusb-system_db_1
```
