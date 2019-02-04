from Crypto.Cipher import AES
from Crypto import Random
import socket, time

#variables of the server
hostname = '172.16.150.128'
port = 8888

#socket made and connected to the server
s = socket.socket()
s.connect((hostname, port))

#made two random values for the AES cipher and stored in variables, because it is possible to send those variables to the server
key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)
#AES cipher made of those two random variables
aes = AES.new(key, AES.MODE_CBC, iv)
s.send(key)     #key sent to server(plaintext)
time.sleep(1)
s.send(iv)      #Initialization vector sent to server(plain text)
while(True):
    data = input()          #get data from keyboard
    if(data == 'close' or data == 'Close'):
        data = aes.encrypt(data)    #encrypt data with AES
        s.send(data)                #send it to the server
        time.sleep(1)               #wait for 1 sec
        break                       #jump of the while loop and close connection
    else:
        data = aes.encrypt(data)    #encrypt data with AES
        s.send(data)                #send it to the server
s.close()
