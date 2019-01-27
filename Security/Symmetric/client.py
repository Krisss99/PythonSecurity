from Crypto.Cipher import AES
from Crypto import Random
import socket

hostname = '192.168.178.241'
port = 8888

s = socket.socket()
s.connect((hostname, port))
key = s.recv(16)
iv = s.recv(16)
aes = AES.new(key, AES.MODE_CBC, iv)

while(True):
    data = s.recv(1024)
    print(data)
