from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

#variables of the server
hostname = '172.16.150.128'
port = 8888

#generate AES key and return two random values(they will be send to the server) and return also AES cipher
def generateAES():
    key = Random.new().read(AES.block_size)
    iv = Random.new().read(AES.block_size)
    symmetricKey = AES.new(key, AES.MODE_CBC, iv)
    return key, iv, symmetricKey

#socket object, connect to server and receive public key in PEM form
s = socket.socket()
s.connect((hostname, port))
time.sleep(1)
publicKeyPEM = s.recv(1024)

#import key so it can be used to encrypt key and Initialization vector
publicKey = RSA.importKey(publicKeyPEM)
key, iv, symmetricKey = generateAES()               #make AES cipher but also return two random values needed to make this cipher
key = publicKey.encrypt(key, 32)                    #encrypt secret key with public key
s.send(key[0])                                      #send it to the server
iv = publicKey.encrypt(iv, 32)                      #encrypt Initialization vector with public key
s.send(iv[0])                                       #send it also to the server
while(True):    
    message = input()                               #get input from keyboard
    if(message == 'close' or message == 'Close'):   #if message is close
        message = symmetricKey.encrypt(message)     #encrypt message with AES
        s.send(message)                             #send it to the server
        time.sleep(1)                               #wait for 1 sec and jump off the loop and close connection
        break
    else:
        message = symmetricKey.encrypt(message)     #encrypt with AES
        s.send(message)                             #send it to the server
s.close()
