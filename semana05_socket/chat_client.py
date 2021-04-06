# Ana Júlia Costa Santana
# Matrícula : 11811ETE003

# Semana05 - Programa 2 - Cliente#

import socket
import select
import sys
import threading

from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#criando objeto socket "cliente"

if len(sys.argv) != 3: 
    print ("Uso correto: script, Endereço IP, Número da porta")

IP = input('Insira o IP -->') #nome da máquina local inserida pelo cliente
Port = int(input('Insira a porta -->'))#  Cliente insere a porta reservada
ADDR = (IP, Port)
client.connect(ADDR) 



# my_username = input("Username:")
# # client.setblocking(False)

# username = my_username.encode("utf-8")
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
# client_s.send(username_header+username)


while True:
	sockets_list = [sys.stdin, client] 
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
	
	for socks in read_sockets:
		if socks == client:
			message = socks.recv(2048) 
			print (message) 
		else:
			message = sys.stdin.readline()
			server.send(message) 
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush() 
server.close() 



