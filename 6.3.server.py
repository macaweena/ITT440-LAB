import socket
import sys
import time
# value of each symbol is the corresponding integer value
import errno
#import math library to perform calculation function like LOG, SQUARE ROOT etc
import math
from multiprocessing import Process

mantaperz_message = '\nHTTP/1.0 200 OK\n\n'
nomantaperz_message = '\nHTTP/1.0 404 error\n\n'

def process_start(serversock):
    serversock.send(str.encode("Python Calculator (LOG <log>, SQUARE ROOT <sqrt>, EXPONENTIAL <exp>)\n =================================== \n Instruction: log/sqrt/exp <number>\n Example: log >: log 10\n =================================== \n \t\tType 'exit' to close"))
    while True:
        #input from client
	data = serversock.recv(2048)
        data = data.decode("utf-8")

        #calculation
        try:
            mathematic, value = data.split()
            mt = str(mathematic)
            num = int(value)

            if mt[0] == 'l':
                mt = 'Log'
                answer = math.log10(num)
            elif mt[0] == 's':
                mt = 'Square root'
                answer = math.sqrt(num)
            elif mt[0] == 'e':
                mt = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('LOST!')

            sendAnswer = (str(mt) + '(' + str(num) + ') = ' + str(answer))
            print ('>>>>>>>>>>>>>>> \n Calculation completed! Result sent! \n>>>>>>>>>>>>>>>')
        except:
            print ('wrong input!')
            sendAnswer = ('wrong input!')

        

        if not data:
            break

        serversock.send(str.encode(sendAnswer))
        
    serversock.close()
	
if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #port connected
    server.bind(("",8828))
    print("connecting to client ...")
    server.listen(28)

    try:
        while True:
            try:
                serversock, serveraddr = server.accept()
                p = Process(target=process_start, args=(serversock,))
                p.start()

            except socket.error:

                print('ERROR!')

            except Exception as err:
                print("INTERRUPT!")
                print(err)
                sys.exit(1)
    finally:
           s.close()
