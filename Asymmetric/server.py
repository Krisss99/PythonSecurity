from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

#variables of the server
hostname = '172.16.150.128'
port = 8888
numberOfClients = 1

#socket and binding ip and port, listening to max numberOfClients
s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)

c, addr = s.accept()                                        #accepting connection from the client
connection = True           
print(f'Got connection from {addr}')                        #got connetion from the client(show ip)
privateKey = RSA.generate(2048, Random.new().read)          #make private key
publicKey = privateKey.publickey()                          #make public key from the private key
publicKeyPEM = publicKey.exportKey(format='PEM')            #export public key to plain text
c.send(publicKeyPEM)                                        #send public key to the server
while(connection == True):                                  
    encrypted = c.recv(1024)                                #encrypted data is received en stored in variable
    message = privateKey.decrypt(encrypted)                 #data is decrypted with private key
    message = message.decode()                              #message is decoded from bytes to string
    print(message)                                          #message printed
    if(message == 'close' or message == 'Close'):           #if message is close, close connection
        connection = False
c.close()
