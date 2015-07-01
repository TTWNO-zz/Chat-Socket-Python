import socket

iphost = raw_input('Enter the Server IP: ')
nameuser = raw_input('Username: ')

socket = socket.socket()
socket.connect((iphost, 6969))
print "INF: you can write 'close' without quotes to close."

while True:
	mensaje = raw_input('Message: ')
	datos= nameuser + ": " + mensaje
	socket.send(datos)
	if mensaje == 'close':
		socket.close()

	print "Awaiting message..."
	datos = socket.recv(1000)
	print datos
