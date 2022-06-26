import socket
import os
import csv
import sys

# encryption and decryption 
from cryptography.fernet import Fernet

Csocket = socket.socket()
host = '192.168.56.101'
port = 9999

# anywhere safe // key generation
key = Fernet.generate_key()

# string the key into file//generate and saave the key
with open ('filekey.key', 'wb')as filekey:
	key = filekey.write(key)
print ('connecting...')
try:
	Csocket.connect((host, port))
	# receive text up to 2048 bytes
	tinker = Csocket.recv(2048)
	print (tinker)

# catcing exception/error
except socket.error as err:
	print (str(err))

# welcome menu
	def menu():
		print ("********* please choose your command ^^ *********")
		print ()

# choose your menu
		choice = input ("""
					A: upload file
					B: download file
					C: quit\n

					enter your choice: """)

# Get the current working
# directory (CWD)
	path = os.getcwd()
	menu()
	if choice == "A" or choice == "a":
		while True:
				enter_cmd = input("Type a command >> ")
				Csocket.send(str.encode(enter_cmd))
				# using split to split string ino list
				if enter_cmd.split(" ")[0] == "Upload file":
					filename = enter_cmd.split(" ")[1]
					if os.path.isfile(filename):
						with open('filekey.key', 'rb') as filekey:
							#opening the key
							key = filekey.read()
						# using the generated key
						fernet = Fernet(key)
						# opening the original file to encrypt
						with open(filename, 'rb') as file:
    							original = file.read()
						# encrypting the file
						encrypted = fernet.encrypt(original)
						# opening the file in write mode and
						# writing the encrypted data
						with open(filename, 'wb') as encrypted_file:
							encrypted_file.write(encrypted)
							Csocket.sending(bytes(enter_cmd, "utf-8"))
						f = open(filename, 'rb')
						contents = f.read(2048)
						Csocket.send(encrypted)
						tinker = Csocket.recv(2048)
						print (tinker)
						print ("Succesfully stored\n")
						f.close()
					else:
						print("wrong!!!!\n")
	elif choice == "B" or choice == "b":
		while True:
				if enter_cmd.split(" ")[0] == "downloading":
					Csocket.sendall(bytes(enter_cmd, "utf-8"))
					buffer = Csocket.recv(2048)
					buffer.decode() == "No file found"
					os.system("cls")
					menu()
					print ("wrong!!!\n")
				else:
					tinker = Csocket.recv(2048)
					print (tinker)
					print ("received successfully\n")
					f = open(enter_cmd.split(" ")[1], "wb")
					f.write(buffer)
					f.close()
					input = buffer.decode()
	elif choice == "C" or choice == "c":
		while True:
				if enter_cmd.split(" ")[0] == "Quit":
					print ("Disconnected")
					Csocket.sendall(bytes("Quit", "utf-8"))
					Csocket.close()
					break
				else:
					print ("invalid command, try one more time.\n")
					menu()
