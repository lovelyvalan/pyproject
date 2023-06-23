print('SERVER SOCKET')
import socket
from pickle import dumps,loads
import threading
# server socket ---> who use bind and listen

def recv_from_client():
    global conn,connected

    while(connected):
        data=conn.recv(1024)
        print('Received data from client : ',loads(data))

x=socket.socket()  # initializing socket
port,host=55555,'127.0.0.1'
x.bind((host,port))
x.listen(5),print('listening...')          # waiting for connection


clients=[]
i=0
while i< 2:
    conn,addr=x.accept()
    clients.append((conn,addr))
    print('client connected',addr)
    i += 1

connected=True

i = 0
while True:
    i += 1
    conn,addr=clients[i%2]
    conn.sendall(dumps(1))
    data = conn.recv(1024)
    data=loads(data)
    print('received from client ',(i%2),(data))
    # data fetch from datastore
