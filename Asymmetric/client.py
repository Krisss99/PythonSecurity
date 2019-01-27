from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

hostname = '192.168.178.241'
port = 8888
s = socket.socket()
s.connect((hostname, port))
time.sleep(1)
publicKeyPEM = s.recv(1024)
print(publicKeyPEM)
publicKey = RSA.importKey(publicKeyPEM)
while(True):
    message = input()
    if(message == 'close' or message == 'Close'):
        encrypted = publicKey.encrypt(message.encode(), 32)
        s.send(encrypted[0])
        time.sleep(1)
        break
    else:
        encrypted = publicKey.encrypt(message.encode(), 32)
        s.send(encrypted[0])
s.close()
