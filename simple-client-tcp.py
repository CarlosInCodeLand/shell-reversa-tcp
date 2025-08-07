import socket

# Solicita ao usuário o IP do servidor
IP = input("Digite o IP: ")
# Solicita ao usuário a porta do servidor
PORTA = input("Digite a porta: ")

# Cria um socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta conectar ao servidor com o IP e porta informados
    client.connect((IP, int(PORTA)))
    # Envia uma mensagem ao servidor
    client.send(b"Ola!")
    # Recebe a resposta do servidor (até 10240 bytes)
    resposta = client.recv(10240).decode()
    # Exibe a resposta recebida
    print(resposta)
except Exception as e:
    # Em caso de erro, exibe a mensagem de erro
    print(f"Erro! {e}")