import socket
import time

hostname = '172.16.150.128'
port = 8888
s = socket.socket()
s.connect((hostname, port))


while(True):
    data = input()
    if(data == 'close' or data == 'Close'):
        s.send(data.encode())
        time.sleep(1)
        break
    else:
        s.send(data.encode())
s.close()
