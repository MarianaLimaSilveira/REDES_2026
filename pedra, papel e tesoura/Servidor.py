# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

#Aguarda que os jogadores entrem
    print("[server] Aguardando jogador 1")
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[server] OK. Você é o jogador 1".encode())
    print("[server] Aguardando jogador 2")

    print("Aguardando jogador 2")
    conn_2, addr_2 = s.accept() 
    conn_2.sendall("[server] OK. Você é o jogador 2".encode())

    
    for i in range(3):
        conn_2.sendall("[server] Aguarde a jogada do outro jogador".encode())
        conn_1.sendall("[server] Faça sua jogada".encode())
        msg_1 = conn_1.recv(1024).decode()
        conn_1.sendall("[server] Aguarde a jogada do outro jogador".encode())
        print("Jogador 1 fez sua jogada!")
        

    
        conn_2.sendall("[server] Faça sua jogada".encode())
        msg_2 = conn_2.recv(1024).decode()
        print("jogador 2 fez sua jogada!")

        conn_2.sendall("[server] Exibindo resultados".encode())
        conn_1.sendall("[server] Exibindo resultados".encode())
        print("Exibindo Resultados:")
        print("Jogador 1 jogou: " + msg_1)
        print("Jogador 2 jogou: " + msg_2)
               
        conn_1.sendall("jogada jogador 1:" + msg_1.encode())
        conn_1.sendall("jogada jogador 2:" + msg_2.encode())

        conn_2.sendall("jogada jogador 1:" + msg_1.encode())
        conn_2.sendall("jogada jogador 2:" + msg_2.encode())


    conn_1.close()
    conn_2.close()

    