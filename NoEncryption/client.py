import socket
import time

#hostname and port of the server 
hostname = '172.16.150.128'
port = 8888

s = socket.socket()             #making socket     
s.connect((hostname, port))     #connecting to given address and port


#get data from keyboard, and send it to the server
while(True):
    data = input()
    if(data == 'close' or data == 'Close'):
        s.send(data.encode())
        time.sleep(1)
        break
    else:
        s.send(data.encode())
s.close()
