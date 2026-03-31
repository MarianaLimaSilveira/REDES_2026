import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002

LETRA = ''

CEP = ["", ""]
NOME = ["", ""]

semaforo = threading.Semaphore(0)


def atender_cliente(conn, addr,tid):
    
    semaforo.acquire()

    #envia letras sorteadas
    with conn:
        conn.sendall(LETRA.encode())
        #envia mesagem
        conn.sendall("CEP:".encode())
        #aguarda resposta
        resposta = conn.recv(1024).decode("")
        #print(f"Cliente {tid} respondeu: {resposta}")
        CEP[tid] = resposta

        conn.sendall("Nome:".encode())
        resposta = conn.recv(1024).decode("")
        NOME[tid] = resposta


def iniciar_servidor():
    global CEP
    global LETRA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

        
        conn1, addr1  = server.accept()
        thread1 = threading.Thread(target=atender_cliente,args=(conn1, addr1), daemon=True)
        thread1.start()
        
        conn2, addr2  = server.accept()
        thread2 = threading.Thread(target=atender_cliente,args=(conn2, addr2), daemon=True)
        thread2.start()

        #sorteia letra
        LETRA = 'T'
        #libera semáforo
        semaforo.release()
        semaforo.release()

        #aguarda clientes jogarem
       # for sem_i in semaforos_jogadas:
          #  sem_i.aquire()

        #printa jogadas dos clientes
        print (CEP)
        print (NOME)
        

        #aguarda threads finalizarem 
        thread1.join()
        thread2.join()

if __name__ == "__main__":
    iniciar_servidor()