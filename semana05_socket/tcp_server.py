import socket

IP = socket.gethostbyname(socket.gethostname())
Port = int(input('Insira a porta desejada -->'))
ADDR = (IP, Port)
FORMAT = "utf-8"
SIZE = 1024


print("[STARTING...] O servidor está sendo inicializado")
print('Rodando no IP: '+IP)
print('Rodando na porta: '+str(Port))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[LISTENING...] O servidor está ouvindo")

clientsocket, adress = server.accept()
print(f"[CONNECTION] Nova conexão {adress} estabelecida")
# linha de teste : clientsocket.send(bytes("Bem vindo ao servidor!","utf-8"))

data = clientsocket.recv(SIZE).decode(FORMAT)
print('[RECV...]Enviando dados.',data)

if data != '':
	file = open(data,'rb')
	data = file.read(SIZE)
	clientsocket.send("Nome de arquivo encontrado.".encode(FORMAT))
	while data:
		clientsocket.send(data)
		data = file.read(SIZE)
	
print(f"[RECV...] Arquivo enviado.")
clientsocket.shutdown(socket.SHUT_RDWR)
clientsocket.close()
print(f"[DISCONNECTED..] {adress}")