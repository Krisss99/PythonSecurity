import socket

hostname = '192.168.178.241'
port = 8888
numberOfClients = 1

s = socket.socket()
s.bind((hostname, port))
s.listen(numberOfClients)
c, addr = s.accept()
connection = True
print(f'Got connection from {addr}')
while(connection == True):
    message = c.recv(1024).decode()
    print(message)
    if(message == 'close' or message == 'Close'):
        connection = False
c.close()
