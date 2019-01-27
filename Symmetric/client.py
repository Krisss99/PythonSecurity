from Crypto.Cipher import AES
from Crypto import Random
import socket, time

hostname = '192.168.178.241'
port = 8888
s = socket.socket()
s.connect((hostname, port))
key = Random.new().read(16)
iv = Random.new().read(16)
aes = AES.new(key, AES.MODE_CBC, iv)
print(key)
print(iv)
s.send(key)
time.sleep(1)
s.send(iv)
while(True):
    data = input()
    if(data == 'close' or data == 'Close'):
        data = aes.encrypt(data)
        s.send(data)
        time.sleep(1)
        break
    else:
        data = aes.encrypt(data)
        s.send(data)
s.close()
