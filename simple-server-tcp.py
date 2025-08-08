import socket

IP = "0.0.0.0"
PORTA = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open("output.txt", "w")

try:
    server.bind((IP, PORTA))
    server.listen(5)
    print("Listening...")

    client_socket, addres = server.accept()
    print(f"Received from: {addres[0]}")

    data = client_socket.recv(1024).decode()
    file.write(data)

    server.close()
except Exception as e:
    print(f"Erro! {e}")
    server.close()