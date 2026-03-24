import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002

LETRA = "S"

CEP = ["", ""]
NOME = ["", ""]

semaforo = threading.Semaphore(0)

def atender_cliente(conn, addr):

    semaforo.acquire()

    with conn:
        #envia a letra aos clientes
        conn.sendall(LETRA.encode())

        #envia a mensagem ao cliente
        conn.sendall("CEP ".encode())

        #aguarda a resposta
        resposta = conn.recv(1024).decode()
        print("cliente "(tid) "respondeu: " (resposta.decode()))

        conn.sendall("CEP: ".encode)
        resposta = conn.recv(1024).decode()
        CEP[tid] = resposta

    pass

def iniciar_servidor():
    global CEP
    global LETRA

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

        # aguarda jogador 1
        conn_1.addr_1 = server.accept()
        thread_1 = threading_Thread

        #Aguarda jogador 2
        conn_2.addr_2 = server.accept()
        thread_2 = 

        #Letra

        #Libera o semaforo



        # Aguarda os clientes jogarem
        thread_1.join()
        thread_2.join()



if __name__ == "__main__":
    iniciar_servidor()
