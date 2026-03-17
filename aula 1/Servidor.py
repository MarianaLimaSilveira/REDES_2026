# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9003

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print("Aguardando cliente...")

    conn, addr = s.accept()
    print("Conectado:", addr)

    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                break

            print("Cliente:", data.decode())

            msg = input("Servidor: ")
            conn.sendall(msg.encode())