print('CLIENT SOCKET')
import  socket
from pickle import dumps,loads

# client socket ---> who use connect

y = socket.socket()

port,host=4455,'127.0.0.1'
y.connect((host,port))

#y.sendall(b'this  is the message from client')
# or
data =  dumps([x for x in 'HelloWorld'])
y.sendall(data)