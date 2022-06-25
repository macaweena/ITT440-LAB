import socket
import os

#identifier of current thread
from _thread import*

#encrypting
from cryptography.fernet import Fernet

SSocket = socket.socket()
host = ''
port = 8080
ThreadCount = 0
#key generating
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
	filekey.write(key)
try:
	#socket class assigns an IP address and a port number
	SSocket.bind((host, port))
#traps the error
except socket.error as err:
	print (str(err))
print ("Connection ...\n")
#Listen for connections made to the socket
SSocket.listen(5)

def threaded_client(connection):
	connection.send(str.encode('Welcome To The Storage Server'))
	while True:
		data = connection.recv(2048)
		input = data.decode()
		if input.split(" ")[0] == "Quit":
			print ("Client ", address[0], "disconnected...\n")
			Client.close()

		elif  input.split(" ")[0] == "Uploaded":
			fernet = Fernet(key)
			with open(input.split(" ")[1], 'rb') as myenc_file:
				encrypted = myenc_file.read()
				encrypted = myenc_file.read()
			decrypted = fernet.decrypt(encrypted)
			print ("File Is Uploading")
			buffer = connection.recv(2048)
			print ("File Successful Upload\n")
			connection.send(str.encode('Server: Successful Uploading'))
			with open(input.split(" ")[1], 'wb') as mydec_file:
				mydec_file.write(decrypted)
			f.close()
			input = buffer.decode()
		elif input.split(" ")[0] == "downloaded":
			filename = input.split(" ")[1]
			print ("file name", filename)
			if os.path.isfile(filename):
				with open (filename, 'rb') as f:
					init = f.read(2048)
					while init:
						connection.send(init)
						init = f.read(2048)
					print ("sendind\n")
					connection.send(str.encode('Server: Successful Sending'))
				f.close()
			else:
				print ("invalid")
				connection.send(bytes("Not A Valid Command", "utf-8"))
				break
	while True:
		Client, address = SSocket.accept()
		print ('Connected to: ' + address[0] + ':' + str(address[1]))
		start_new_thread (threaded_client, (Client, ))
		ThreadCount += 1
		print ('Thread Number: ' + str(ThreadCount))
	SSocket.close()

