import socket
import threading
from time import sleep
 
HOST = "127.0.0.1"
PORT = 9002

mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    
    letra = cliente.recv(1024).decode()
    print("letra sorteada:", letra)

    #CEP
    mensagem = cliente.recv(1024).decode()
    resposta = input(mensagem)
    cliente.sendall(resposta.decode())

    #NOME
    mensagem = cliente.recv(1024).decode()
    resposta = input(mensagem)
    cliente.sendall(resposta.decode())