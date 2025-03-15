import socket
from datetime import datetime

def fibonacci(N):
    if N == 1 | N == 2:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

def iniciar_Servidor():

    HOST = "localhost"
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT))
        S.listen()
        print(f"Servidor executando em {HOST}:{PORT}")
        while True: 
            conn, addr = S.accept()
            with conn:
                print(f"Conexão com {addr} estabelecida.")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode().strip().lower() == "data e hora":
                        agora = datetime.now().strftime("%y - %m - %d %H:%M:S")
                        resposta = f"Data e hora: {agora}"
                        conn.sendall(resposta.encode())
                    elif data.decode().strip().lower() == "bom dia":
                        resposta = f"Olá, {addr}"
                        conn.sendall(resposta.encode())

                    elif data.decode().strip().lower() == "fatorial":
                        resposta = "número"
                        conn.sendall(resposta.encode())
                        data = conn.recv(1024)
                        N = int(data.decode())

                        Fatorial = 1
                        for x in range(N):
                            Fatorial = Fatorial * (x + 1)
                        
                        resposta = f"O fatorial de {N} é {Fatorial}"
                        conn.sendall(resposta.encode())

                    elif data.decode().strip().lower() == "fibonacci":
                        resposta = "número"
                        conn.sendall(resposta.encode())
                        data = conn.recv(1024)
                        N = int(data.decode())
                        F = fibonacci(N)
                        
                        resposta = f"O fibonacci de {N} é {F}"
                        conn.sendall(resposta.encode())
                    else: 
                        resposta = "Mensagem inválida"
                        conn.sendall(resposta.encode())

if __name__ == "__main__":
    iniciar_Servidor()