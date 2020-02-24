# Pomodoro back


El desarrollo es un API para mostrar el funcionamiento de la técnica pomodoro 
, desarrollada con Python + Django y Django Rest Framework para el API.

Para desplegar la aplicación en local lo primero que tendremos que hacer es descargar la rama master de este repositorio.
Seguidamente sería recomendable crear un entorno virtual, para instalar en el las dependencias del api, descritas en el fichero 
requeriments.txt. Para ello lanzaremos el comando pip install -r requeriments.txt.
Seguidamente tendremos que realizar la migración de los modelos de la base de datos mediante el comando  
python manage.py makemigrations y aplicar estos cambios mediante el comando python manage.py migrate.
Por último es recomendable crear un usuario administrador para la herramienta de administración de Django mediante el comando python manage.py createsuperuser.
De esta forma podrá acceder al admin de Django mediante la url http://localhost:8000/admin/.


### Urls de prueba para el API REST


API de usuarios

Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.

```bash
POST http://localhost:8000/api/1.0/users/
{
    "first_name": "aaaaa",
    "last_name": "aaaaa",
    "username": "aaaaaa",
    "email": "aaaaa@aaa.com",
    "password": "aaaaaa"
}
```
Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un usuario el propio usuario o un administrador.

```bash
GET http://localhost:8000/api/1.0/users/<id_user>
```
Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.
```bash
PUT http://localhost:8000/api/1.0/users/<id_usuario>
{
    "first_name": "aaaaa",
    "last_name": "aaaaa",
    "username": "aaaaaaa",
    "email": "aaaaaaaaa",
    "password": "aaaaaaaaa"
}
```
API de Tareas

Un endpoint que devuelva las tareas de un usuario y un estado concretos
```bash
GET http://localhost:8000/api/1.0/tasks/?userid=10&end_task=True
```
Un endpoint que permite crear tareas de un usuario
```bash
POST http://localhost:8000/api/1.0/tasks/
{
    "user": 10,
    "description": "Tarea prueba XX",
    "pub_date": "2020-02-23T12:59:47.806000Z",
    "number_pomodoro_used": 1,
    "end_task": true
}
```
Un endpoint que permite modificar tareas de un usuario
```bash
PATCH http://localhost:8000/api/1.0/tasks/<id_task>/
{
    "userid": 10,
    "number_pomodoro_used": 14
}
```


## Version



 V1.0
