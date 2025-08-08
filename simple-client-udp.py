import socket

IP = input("Digite o IP: ")
PORTA = input("Digite a porta: ")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria um socket UDP

try:
    while True:
        msg = input('Mensagem: ') + "\n"
        client.sendto(msg.encode(), (IP, int(PORTA)))        # Envia a mensagem para o servidor

        data, sender = client.recvfrom(1024)        # Recebe a resposta do servidor (até 1024 bytes)
        print(sender[0] + ':' + data.decode())       # Exibe o IP do remetente e a mensagem recebida

        if msg == "/sair" or data.decode() == "/sair":
            break
    client.close()
except Exception as e:
    print(f"Erro! {e}")
    client.close()
