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
BUFFER_SIZE = 1024
HEADER_LENGTH = 10


my_username = input("Username:")
client.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_s.send(username_header+username)


while True:
	sockets_list = [sys.stdin, server] 
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
	message = input(f"{my_username} > ")

	if message:
		message = message.encode("utf-8")
		message_header = f"{len(message):< {HEADER_LENGTH}}".encode("utf-8")
		client_s.send(message_header + message)
	try:
		while True:
			#receive things
			username_header = client_s.recv(HEADER_LENGTH)
			if not len(username_header):
				print("Conncection closed by the server")
				sys.exit()
			username_length = int(username_length.decode("utf-8").strip())
			username = client_s.recv(username_length).decode("utf-8")

			message_header = client_s.recv(HEADER_LENGTH)
			message_length = int(message_header.decode("utf-8").strip())
			message = client_s.recv(message_length).decode("utf-8")

			print(f"{username} > {message}")

	except IOError as e :
		if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
			print('Reading error',str(e))
			sys.exit()
		continue

	except Exception as e:
		print('General error',str(e))
		sys.exit()




