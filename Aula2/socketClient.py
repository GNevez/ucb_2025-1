import socket;

def iniciar_Cliente():

        HOST = "localhost"
        PORT: 65432

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
            S.connect((HOST, PORT))
            print("Solicitando Data e hora...")
            S.sendall(b"data e hora")
            data = S.recv(1024).decode()
            print(f"Resposta do servidor: {data}")

if __name__ == "__main__":
    iniciar_Cliente()