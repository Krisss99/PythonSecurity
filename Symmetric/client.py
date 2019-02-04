from Crypto.Cipher import AES
from Crypto import Random
import socket, time

hostname = '172.16.150.128'
port = 8888
s = socket.socket()
s.connect((hostname, port))
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
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
