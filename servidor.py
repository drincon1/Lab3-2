# Código que representa la aplicación servidor UDP
import socket
import time
import os
import sys
import threading
from datetime import datetime
import time

#IP = 'localhost'
IP = '172.16.21.129'
PORT = 7000
ruta_archivo = ""
barrier = None
servidor = None


def thread_function(client_address):
    tName = threading.current_thread().getName()
    pservidor(f'El {tName} se ha conectado en el puerto {client_address[1]}')
    # pservidor(f'Se enviará al {tName} el archivo en la ruta: {ruta_archivo}')
    pservidor(f'{tName} esperando')
    barrier.wait()

    buffSize = 8192
    c = 0
    sizeS = os.stat(ruta_archivo)
    sizeSS = sizeS.st_size  # tamaño en bytes
    NumS = int(sizeSS / buffSize)
    NumS = NumS + 1

    check = int(NumS)
    archivo = open(ruta_archivo, "rb")
    pservidor(f'Inicio de envio de paquetes al cliente {tName}')
    aviso = True
    starttime = time.time()
    lasttime = starttime
    
    
    while check != 0:
        paquete = archivo.read(buffSize)
        servidor.sendto(paquete, client_address)
        c += 1
        check -= 1
        porcentaje = (c/NumS)*100 // 1
        if porcentaje == 50 and aviso == True:
            pservidor(f'Se han enviado {porcentaje}% paquetes al cliente {tName}')
            aviso = False
            
    laptime = round((time.time() - lasttime), 2)       
    pservidor(f'Todo los paquetes enviados a {tName}')
    archivo.close()
    
    now = datetime.today()
    ruta = f'Logs/S-{tName}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.txt'
    file = open(ruta, "w")
    file.write(f'Nombre del archivo: {ruta_archivo[-9:]}\nTamaño: {ruta_archivo[-9:-4]}\nCliente: {tName}\nTiempo: {laptime}')
    file.close()
    

def pservidor(msj):
    print(f"[SERVIDOR] {msj}")


def main():
    # CONFIGURACIÓN DE LA APLICACIÓN SERVIDOR
    global ruta_archivo
    global barrier
    global servidor
    # Definir con cuál archivo se trabajará
    res_archivo = input('¿Cual archivo desea recibir sus clientes?\n[1] 100 MB\n[2] 250 MB\n')
    # if para establecer la ruta
    if int(res_archivo) == 1:
        ruta_archivo = "archivos_servidor/100MB.txt"

    elif int(res_archivo) == 2:
        ruta_archivo = "archivos_servidor/250MB.txt"
    else:
        ruta_archivo = "archivos_servidor/prueba.txt"


    # Cuántos clientes se manejaran
    num_clientes  = int(input('¿Cuántos clientes quiere conectados?\nOpciones válidas: 1,5,10\n'))

    barrier = threading.Barrier(num_clientes)
    size = os.stat(ruta_archivo)
    sizeSS = size.st_size
    pservidor(f'Tamaño del archivo en bytes: {str(sizeSS)}')
    pservidor(f'El número de paquetes serán: {sizeSS/64000}')

    # CREACIÓN E INICIALIZACIÓN DEL SERVIDOR
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pservidor('Inicializado')
    servidor.bind((IP, PORT))
    pservidor('Esperando conexiones')
    data = servidor.recvfrom(1024)

    info = data[0].decode('utf-8')

    if info == "CONFIG":
        pservidor('Se ha recibido la solicitud para configurar la aplicación CLIENTE')
        servidor.sendto(f'{ruta_archivo}@{num_clientes}@{sizeSS}'.encode('utf-8'),data[1])
        pservidor(f'Se ha enviado la información para configurar la aplicación CLIENTE a través de: {data[1]}')
    else:
        pservidor(f'No se ha recibido la información correcta\nSe ha recibido: {data}')

    # FIN CONFIGURACIÓN DE LA APLICACIÓN SERVIDOR

    i = 1
    while True:
        data, client_address = servidor.recvfrom(1024)
        cliente = threading.Thread(target=thread_function, name="Cliente "+str(i),args=(client_address,))
        cliente.start()
        i=i+1


    servidor.close()
    #pservidor('Conexiones cerradas')




if __name__ == '__main__':
    main()
