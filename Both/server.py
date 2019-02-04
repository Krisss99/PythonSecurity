from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, time

#server variables
hostname = '172.16.150.128'
port = 8888
numberOfClients = 1
connection = True

#generate RSA keys, public and private, but also make public key exportible to be sent
def generateRSA():
    privateKey = RSA.generate(2048, Random.new().read)
    publicKey = privateKey.publickey()
    publicKeyPEM = publicKey.exportKey(format='PEM')
    return privateKey, publicKey, publicKeyPEM

#generate AES cipher using key and Initialization vector
def generateAES(key, iv):
    symmetricKey = AES.new(key, AES.MODE_CBC, iv)
    return symmetricKey

#making socket, binding ip and port and listening to max numberOfClients
s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)


c, addr = s.accept()                                            #server accepts connection from client
print(f'Got connection from {addr}')                            #info printed that server got connection from some ip address
privateKey, publicKey, publicKeyPEM = generateRSA()             #make the RSA keys but also public key in PEM form(to be exported)
c.send(publicKeyPEM)                                            #send the public key(PEM form) to the client
encryptedKey = c.recv(1024)                                     #get secret key for the AES(encrypted with sent public key)
encryptedIv = c.recv(1024)                                      #get Initialization vector for the AES(encrypted with sent public key)  
key = privateKey.decrypt(encryptedKey)                          #decrypt secret key with own private key
iv = privateKey.decrypt(encryptedIv)                            #decrypt Initialization vector with own private key
symmetricKey = generateAES(key, iv)                             #generate AES cipher (symmetric encryption)
while(connection == True):
    encrypted = c.recv(1024)                                    #get symmetric encrypted data(AES)
    message = symmetricKey.decrypt(encrypted)                   #decrypt it with AES
    message = message.decode()                                  #from bytes to string
    print(message)                                              #print message
    if(message == 'close' or message == 'Close'):               #if message is close -> out of loop, close connection
        connection = False
c.close()
