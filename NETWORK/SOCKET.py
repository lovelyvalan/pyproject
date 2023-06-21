print('SERVER SOCKET')
import socket
from pickle import dumps,loads
# server socket ---> who use bind and listen

x=socket.socket()  # initializing socket
port,host=4455,'127.0.0.1'
x.bind((host,port))
x.listen(5),print('listening...')          # waiting for connection
conn,addr=x.accept()
print('Connected to Client',(conn,addr))

data = conn.recv(1024)
data = loads(data)
print('client sent this data ---> ',data)

x.close()
print('Connection Established')