from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

hostname = '192.168.178.241'
port = 8888
numberOfClients = 1
s = socket.socket()

def generateRSA():
    privateKey = RSA.generate(2048, Random.new().read)
    publicKey = privateKey.publickey()
    publicKeyPEM = publicKey.exportKey(format='PEM')
    return privateKey, publicKey, publicKeyPEM

def generateAES(key, iv):
    symmetricKey = AES.new(key, AES.MODE_CBC, iv)
    return symmetricKey
    
    
s.bind((hostname, port))
s.listen(numberOfClients)
c, addr = s.accept()
connection = True
print(f'Got connection from {addr}')
privateKey, publicKey, publicKeyPEM = generateRSA()
print(publicKeyPEM)
c.send(publicKeyPEM)
key = c.recv(1024)
iv = c.recv(1024)
print(key)
print(iv)
symmetricKey = generateAES(key, iv)
while(connection == True):
    encrypted = c.recv(1024)
    message = symmetricKey.decrypt(encrypted)
    message = message.decode()
    print(message)
    if(message == 'close' or message == 'Close'):
        connection = False
c.close()
