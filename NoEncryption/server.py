import socket

hostname = '172.16.150.128'
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
