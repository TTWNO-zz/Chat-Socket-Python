import socket

iphost = raw_input('Introduce la IP Servidor: ')
nameuser = raw_input('Nombre a utilizar: ')

socket = socket.socket()
socket.connect((iphost, 6969))
print "INF: puedes escribir 'close' sin comillas para cerrar."

while True:
	mensaje = raw_input('Mensaje: ')
	datos= nameuser + ": " + mensaje
	socket.send(datos)
	if mensaje == 'close':
		socket.close()

	print "Esperando mensaje..."
	datos = socket.recv(1000)
	print datos
