import socket

#variables of the server
hostname = '172.16.150.128'
port = 8888
numberOfClients = 1

s = socket.socket()                     #making socket object
s.bind((hostname, port))                #combine hostname address and port to a socket
s.listen(numberOfClients)               #server listen to max numberOfClient
c, addr = s.accept()                    #server accepts client
connection = True
print(f'Got connection from {addr}')    #print got connection from {client address}
#if someone is connected, then receive messages
while(connection == True):
    message = c.recv(1024).decode()
    print(message)
    if(message == 'close' or message == 'Close'):
        connection = False
c.close()
