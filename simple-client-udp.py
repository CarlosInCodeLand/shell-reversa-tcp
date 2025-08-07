import socket

# Solicita ao usuário o IP do servidor
IP = input("Digite o IP: ")
# Solicita ao usuário a porta do servidor
PORTA = input("Digite a porta: ")

# Cria um socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # Solicita a mensagem do usuário
        msg = input('Mensagem: ') + "\n"
        # Envia a mensagem para o servidor
        client.sendto(msg.encode(), (IP, int(PORTA)))
        # Recebe a resposta do servidor (até 1024 bytes)
        data, sender = client.recvfrom(1024)
        # Exibe o IP do remetente e a mensagem recebida
        print(sender[0] + ':' + data.decode())
        # Se a mensagem enviada ou recebida for "/sair", encerra o loop
        if msg == "/sair" or data.decode() == "/sair":
            break
    # Fecha o socket após sair do loop
    client.close()
except Exception as e:
    # Em caso de erro, exibe a mensagem de erro e fecha o socket
    print(f"Erro! {e}")
    client.close()
