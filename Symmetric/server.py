from Crypto.Cipher import AES
from Crypto import Random
import socket, time

#variables of the server
hostname = '172.16.150.128'
port = 8888
numberOfClients = 1

#making socket and binding its own ip address and a free port, listens to max numberOfClients(1)
s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)

#accepts connection from client
c, addr = s.accept()
connection = True                      
print(f'Got connection from {addr}')                #print message that connection is established from certain ip address
key = c.recv(1024)                                  #secret key received from the client(sent plain text)
iv = c.recv(1024)                                   #Initialization vector from the client(sent plain text)
aes = AES.new(key, AES.MODE_CBC, iv)                #make AES cipher from those values(the same as the client has)
while(connection == True):                      
    encrypted = c.recv(1024)                        #receive data from client(encrypted)
    message = aes.decrypt(encrypted)                #decrypt data
    print(message.decode())                         #print message 
    if(message == 'close' or message == 'Close'):   #if message is close, connection is set to false and it jumps off the while loop and closes the connection
        connection = False
c.close()
