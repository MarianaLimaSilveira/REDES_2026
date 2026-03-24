import socket

HOST = "127.0.0.1"
PORT = 9002

mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:  #criando o socket pra conectar com o servidor
    cliente.connect((HOST, PORT)) #conecta
    cliente.sendall(mensagem.encode("utf-8"))

    resposta = cliente.recv(1024).decode("utf-8")  #esperando o servidor responder
    print(f"[Server] {resposta}")