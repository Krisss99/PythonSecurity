from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

#variables of the server
hostname = '172.16.150.128'
port = 8888

#socket object and connecting to server
s = socket.socket()
s.connect((hostname, port))

time.sleep(1)                                                   #wait for 1 sec
publicKeyPEM = s.recv(1024)                                     #receive public key from the server  
publicKey = RSA.importKey(publicKeyPEM)                         #import the key so it can be used to encrypt data
while(True):
    message = input()                                           #get data from keyboard
    if(message == 'close' or message == 'Close'):               #if message close: encrypt with public key, send it and jump out of while loop -> closing the connection
        encrypted = publicKey.encrypt(message.encode(), 32)
        s.send(encrypted[0])
        time.sleep(1)
        break
    else:
        encrypted = publicKey.encrypt(message.encode(), 32)     #encrypt with public key, data must be bytes, second parameter just a random number
        s.send(encrypted[0])                                    #send just first position of the tuple(the encrypted data, second position of tuple is empty)
s.close()
