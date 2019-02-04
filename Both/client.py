from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

hostname = '172.16.150.128'
port = 8888
s = socket.socket()

def generateAES():
    key = Random.new().read(AES.block_size)
    iv = Random.new().read(AES.block_size)
    symmetricKey = AES.new(key, AES.MODE_CBC, iv)
    return key, iv, symmetricKey

s.connect((hostname, port))
time.sleep(1)
publicKeyPEM = s.recv(1024)
print(publicKeyPEM)
publicKey = RSA.importKey(publicKeyPEM)
key, iv, symmetricKey = generateAES()
key = publicKey.encrypt(key, 32)
s.send(key[0])
iv = publicKey.encrypt(iv, 32)
s.send(iv[0])
while(True):
    message = input()
    if(message == 'close' or message == 'Close'):
        message = symmetricKey.encrypt(message)
        s.send(message)
        time.sleep(1)
        break
    else:
        message = symmetricKey.encrypt(message)
        s.send(message)
s.close()
