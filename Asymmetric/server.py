from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

hostname = '172.16.150.128'
port = 8888
numberOfClients = 1

s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)
c, addr = s.accept()
connection = True
print(f'Got connection from {addr}')
privateKey = RSA.generate(2048, Random.new().read)
publicKey = privateKey.publickey()
publicKeyPEM = publicKey.exportKey(format='PEM')
print(publicKeyPEM)
c.send(publicKeyPEM)
while(connection == True):
    encrypted = c.recv(1024)
    message = privateKey.decrypt(encrypted)
    message = message.decode()
    print(message)
    if(message == 'close' or message == 'Close'):
        connection = False
c.close()
