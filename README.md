# Lab3-2
Laboratorio 3-2 de Infraestructura de comunicaciones
# Preparación del ambiente
# Instrucciones para correr el código
# lab3-1
# lab3-1
En este archivo se hará una descripción de cómo funcionan las aplicaciones servidor.py y cliente.py. Es necesario leer cada sección para evitar cualquier error.

0. Preparación de ambiente
En este sección se hablará de qué se debe hacer para preparar el ambiente de la aplicación. 
0.1. Verificación de archivos
Donde se vaya a correr el servidor (servidor.py) es necesario verificar que esten las carpetas "archivos_servidor" y "Logs". En la primera carpeta se debe contener los dos archivos 100MB.txt y 250MB.txt. Estos archivos son los que se usaran para hacer las pruebas. En caso de que no existan estos archivos ir a la sección 0.3. La segunda carpeta es donde se guardarán los logs.txt de cada prueba. Por el lado del cliente es necesario que se verifique que esten las carpetas "ArchivosRecibidos" y "Logs". La primera carpeta es donde se guardarán los archivos recibidos del servidor. La segunda  carpeta funcionará de la misma manera que para el servidor.
0.2. Verificación de la IP
En el código de servidor.py es necesario verificar que la variable IP sea la misma que la IP donde se está corriendo el código. Por el lado del cliente.py es necesario verificar que la variable IP tenga el mismo valor a la variable IP del servidor.py
0.3. Generar archivos 100MB y 250MB
0.3.1. Instrucciones 
Para generar estos archivos es necesario estar en la carpeta archivos_servidor en la máquina virtual donde se correrá el servidor. A continuación se mostrará lo que se debe colocar en la terminal para la correcta creación del archivo. Es necesario que el nombre sea el mismo puesto acá para evitar algun fallo. Se presenta cómo se debe hacer para cada sistema operativo.
* Windows: 
  ** Archivo 100MB: fsutil file createnew 100MB.txt 100000000
  ** Archivo 250MB: fsutil file createnew 250MB.txt 250000000
* Mac:
  ** Archivo 100MB: mkfile 100M 100MB.txt
  ** Archivo 250MB: mkfile 250M 250MB.txt
* Linux:
  ** Archivo 100MB: truncate -s 100M 100MB.txt
  ** Archivo 250MB: truncate -s 250M 250MB.txt

1. Correr el código
1.1. Antes de correr
Antes de correr el código es necesario verificar que las carpetas Logs y ArchivosRecibidos esten vacías. Esto con el motivo de poder leer bien las pruebas y verificar que los archivos si fueron recibidos. Esto se debe hacer en ambas máquinas, i.e., en la máquina donde se corre el servidor y la máquina donde se corre el cliente. 
1.2. Correr el código
Es importante primero correr el código servidor.py. Cuando se corre este archivo se deberán responder a unas preguntas de configuración. Luego, el archivo le pedirá que ejecute el archivo cliente.py.
1.3. Finalizar la aplicación
La aplicación cliente.py se finaliza por si sola cuando se haya echo el proceso con cada cliente. Sin embargo, la aplicación servidor.py se debe cerrar de manera manual. Para esto cuando se haya acabado el proceso en la aplicación cliente.py se deberá hacer Ctrl+C en la terminal donde está corriendo servidor.py.

