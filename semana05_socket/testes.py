HEADER_LENGTH = 2048
HEADER_LENGTH = 2048
message = input(f"{my_username} > ")
# Ana Júlia Costa Santana
# Matrícula : 11811ETE003

# Semana05 - Programa 2 - Servidor#


import socket
import sys
import select
import threading
from threading import *


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number") 
 
HEADER_LENGTH = 10
IP = "127.0.0.1"
Port = int(input('Escolha a porta -->'))

print("[STARTING...] O servidor está sendo inicializado")
print('Rodando no IP: '+IP)
print('Rodando na porta: '+ str(Port))

server.bind((IP,Port))
server.listen(100)

clients_list = []


def clientthread(client_socket,addr):
	conn.send("Bem vindo(a) ao chatroom!") #Mensagem de confirmação
	
	while True:
		try:
			message = client_socket.recv(HEADER_LENGTH)
			if message:
				print("<" + addr[0] + ">" + message)
				message_to_send = "<" + addr[0] + "> " + message
				broadcast(message_to_send, client_socket) 

			else:
				remove(client_socket) 
		except:
			continue

def broadcast(message, connection): 
    for clients in clients_list: 
        if clients!= connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
                remove(clients) 

def remove(connection): 
    if connection in clients_list: 
        clients_list.remove(connection) 
  
while True: 
	client_socket, addr = server.accept()
	clients_list.append(client_socket)
	print("Nova conexão" + addr[0] + "aceita")
	start_thread(clientthread,(client_socket,addr))

client_socket.close()
server.close()











