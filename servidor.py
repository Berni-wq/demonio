import socket
import shutil
import os

HOST = "127.0.0.1" 
puerto = 65432 
#levantar el servidor y que reciba las peticiones
def iniciar_servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((HOST, puerto))
    servidor_socket.listen()
    print(f"Servidor escuchando en {HOST}:{puerto}")
    
    while True:
        cliente_socket, direccion_cliente = servidor_socket.accept()
        print(f"Conexión aceptada desde {direccion_cliente}")

        while True:
            datos = cliente_socket.recv(4096)
            if not datos:
                break
            pass
        cliente_socket.close()

#manejar los archivos entre 'entrada y procesado'
def sincronizar_archivos(nombre_archivo):
    ruta_origen = os.path.join("archivos_procesado", "entrada", nombre_archivo)
    ruta_destino = os.path.join("archivos_procesado", "procesado", nombre_archivo)
    
    if os.path.exists(ruta_origen):
        shutil.move(ruta_origen, ruta_destino)
        print(f"Archivo {nombre_archivo} sincronizado y movido a procesado.")
    else:
        print(f"No se encontró el archivo {nombre_archivo} en la carpeta de entrada.")
    pass

#guardas los eventos del server en carpeta 'logs'
def registrar_log(mensaje):

    pass