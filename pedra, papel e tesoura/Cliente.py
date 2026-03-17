# Cliente
import socket

HOST = "127.0.0.1"
PORT = 9003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Conecta com o servidor
    s.connect((HOST, PORT))

    #Recebe mesagem do servidor
    msg = s.recv(1024).decode()
    print(msg)

    while True:
        msg = s.recv(1024).decode()
        print(msg)

        #Manda jogada
        msg = input("Jogador: ")
        s.sendall(msg.encode())

        msg = s.recv(1024).decode()
        print(msg)

