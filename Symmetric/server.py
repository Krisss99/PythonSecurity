from Crypto.Cipher import AES
from Crypto import Random
import socket

hostname = '192.168.178.241'
port = 8888
numberOfClients = 1
key = Random.new().read(16)
iv = Random.new().read(16)
aes = AES.new(key, AES.MODE_CBC, iv)

s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)
c, addr = s.accept()
print(f'Got connection from {addr}')
c.send(key)
c.send(iv)
data = b'Hello World 1234'
while(True):
    aes.encrypt(data)
    c.send(data)
