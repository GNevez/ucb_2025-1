import socket;

def iniciar_Cliente():

        HOST = "localhost"
        PORT = 65432

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
            S.connect((HOST, PORT))

            S.sendall(b"fatorial")
            data = S.recv(1024)
            if data.decode() == "número":
                 S.sendall(b"7")
                 data = S.recv(1024)
                 print(f"Resposta: {data.decode()}")

            S.sendall(b"fibonacci")
            data = S.recv(1024)
            if data.decode() == "número":
                 S.sendall(b"4")
                 data = S.recv(1024)
                 print(f"Resposta {data.decode()}")
if __name__ == "__main__":
    iniciar_Cliente()