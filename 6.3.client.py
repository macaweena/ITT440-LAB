import socket
import signal
import sys

CSocket = socket.socket()
host = '192.168.56.101'
port = 8008

print('connecting to server')
try:
    CSocket.connect((host, port))
except socket.error as err:
    print(str(err))

Answering = CSocket.recv(2048)
print(Answering.decode("utf-8"))
while True:
    Input = input('input: ')

    if Input == 'exit':
        break
    else:
        CSocket.send(str.encode(Input))
        Answering = CSocket.recv(2048)
        print(Answering.decode("utf-8"))

CSocket.close()
