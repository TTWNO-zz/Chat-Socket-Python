import commands
import socket

print "Chat - Interfaces disponibles: "
print commands.getoutput("/sbin/ifconfig | egrep -o '^[a-z].......'")
intfz = raw_input('Introduce la interfaz a utilizar: ')
comand = "/sbin/ifconfig "+intfz+" | egrep -o '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | egrep -v '*(0|255)$'"
iphost = commands.getoutput(comand)
print "La IP del Servidor es: ", iphost
nameuser = raw_input('Nombre a utilizar: ')


server = socket.socket()
server.bind((iphost, 6969))
server.listen(7)
print "INF: puedes escribir 'close' sin comillas para cerrar."

print "Esperando clientes..."
# Aceptamos una conexion, se bloquea hasta que alguien se conecte.
socket_cliente, datos_cliente = server.accept()

llave = 0
while llave == 0:
  print "Esperando mensaje..."
	# Esperamos que el cliente mande un mensaje y lo imprimimos.
	datos = socket_cliente.recv(1000)
	print datos

	mensaje = raw_input('Mensaje: ')
	datos= nameuser + ": " + mensaje
	socket_cliente.send(datos)
	if mensaje == 'close':
		socket_cliente.close()
		server.close() 
