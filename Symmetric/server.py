from Crypto.Cipher import AES
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
key = c.recv(1024)
iv = c.recv(1024)
print(key)
print(iv)
aes = AES.new(key, AES.MODE_CBC, iv)
while(connection == True):
    encrypted = c.recv(1024)
    message = aes.decrypt(encrypted)
    print(message.decode())
    if(message == 'close' or message == 'Close'):
        connection = False
c.close()
