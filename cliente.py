# Código que representa la aplicación cliente
from re import T
import socket
import os
import threading
from datetime import datetime
import time

# ATRIBUTOS
IP = 'localhost'
PORT = 7000
num_clientes = 0
tam_archivo = 0
ruta_archivo = ""
# MÉTODOS
def thread_function(server_address):
    tName = threading.current_thread().getName()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.setblocking(1)

    # Genera conexión con el servidor
    data = "Hola"
    cliente.sendto(data.encode('utf-8'), server_address)
    pcliente(tName, f"Comenzando conexión con el servidor que está en el puerto {server_address[1]}")
    pcliente(tName, f"Conectado por el puerto: {cliente.getsockname()[1]}") 
    ruta = f"ArchivosRecibidos/{tName}-Prueba-{num_clientes}.txt"
    archivo = open(ruta, 'wb')

    buffSize = 8192
    starttime = time.time()
    lasttime = starttime
    paquete, server_address = cliente.recvfrom(buffSize)
    pcliente(tName,'Recibiendo paquetes')
    
    try:
        while(paquete):
            archivo.write(paquete)
            cliente.settimeout(5)
            paquete, server_address = cliente.recvfrom(buffSize)

    finally:
        pcliente(tName,'Se ha finalizado el proceso de recibiento de paquetes')
        laptime = round((time.time() - lasttime), 2)
        archivo.close()
        cliente.close()
        
    tam_arch_recibio = os.stat(ruta).st_size 
    now = datetime.today()
    ruta_log = f'Logs/{tName}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}-{now.second}.txt'
    exitoso = ""
    if tam_arch_recibio == tam_archivo:
        exitoso = "SI"
    else:
        exitoso = "NO"
        
    file = open(ruta_log, "w")
    file.write(f'Nombre del archivo: {ruta_archivo[-9:]}\nTamaño: {ruta_archivo[-9:-4]}\nCliente: {tName}\nTiempo: {laptime}\nBytes esperados: {tam_archivo} B\nBytes recibidos: {tam_arch_recibio} B\nEntrega exitosa: {exitoso}')
    file.close()
    


def pcliente(tName, msj):
    print(f'[{tName}] {msj}')


def main():
    global num_clientes
    global tam_archivo
    global ruta_archivo
    server_address = (IP, PORT)
    # CONFIGURACIÓN DE LA APLICACIÓN CLIENTE
    config = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = "CONFIG"
    config.sendto(data.encode('utf-8'), server_address)

    data = config.recvfrom(1024)
    info = data[0].decode('utf-8').split('@')
    ruta_archivo = info[0]
    num_clientes = int(info[1])
    tam_archivo = int(info[2])
    pcliente('APP', f'Ruta archivo: {ruta_archivo}')
    pcliente('APP', f'Número clientes: {num_clientes}')
    # FIN CONFIGURACIÓN DE LA APLICACIÓN CLIENTE

    for i in range(1, num_clientes+1):
        cliente_t = threading.Thread(target=thread_function, name="Cliente"+str(i), args=(server_address,))  # noqa
        cliente_t.start()


if __name__ == '__main__':
    main()
