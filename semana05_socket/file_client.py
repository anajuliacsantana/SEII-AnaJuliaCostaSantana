import socket

IP_alvo = input('Insira o IP -->') #nome da máquina local inserida pelo cliente
Port_alvo = int(input('Insira a porta -->'))#  Cliente insere a porta reservada
ADDR = (IP_alvo, Port_alvo)
FORMAT = "utf-8"
SIZE = 1024


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando objeto socket "cliente"
client.connect(ADDR)

file_name = input('Insira o nome do arquivo no servidor -->')	
client.send(file_name.encode(FORMAT))
name = input('Insira o nome do arquivo destino -->')	
with open(name,'wb') as f:
	print("[SERVER] O arquivo foi aberto")
	msg = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")
	while True:	
		data = client.recv(SIZE)
		print("[SERVER] Recebendo dados...")
		if not data:
			break
		f.write(data) # escrevendo os dados num arquivo

msg = client.recv(SIZE).decode(FORMAT)
print(f"[SERVER]: Arquivo recebido com sucesso!")
client.shutdown(socket.SHUT_RDWR)
client.close()	