# Aplicacion de Login con Flask
## Crear entorno:
1.- Configuar una instancia EC2 en AWS con Amazon Linux
2.- Selecionamos nuestra EC2 desde Instances, vamos a Security, en el apartado de Security groups
Edit reglas de entrada, abrir puerto 5000.
3.- Configurar Cloud9 
4.- Si no tenemos instalado python, instalamos python
5.- Instalamos Flask:
```
pip install Flask

```
6.- Lanzamos la aplicación con el siguiente comando para que se despliegue:
```
 python3 app.py

```
7.- Desde login probamos el inicio de sesion con las credenciales, Si las credenciales no son correctas lanzara el mensaje de error
```
login: admin
password: admin

```
8.- Para probar nuestro test de prueba de la aplicación realizada con  unittest, lanzamos el siguiente comando:
```
python3 -m unittest discover -s tests
```
