print('CLIENT SOCKET')
# client socket ---> who use connect
import socket
from pickle import dumps, loads

y = socket.socket()
port, host = 55555, '127.0.0.1'
y.connect((host, port))

# y.sendall(b'this  is the message from client')
# or
# data =  dumps([x for x in 'HelloWorld'])
# y.sendall(data)

data = None
connected = True


# ch='1'
# while(ch!='#'):
#     print('Enter data to send')
#     data=input()
#     y.sendall(dumps(data))

def visit_on_host():
    global y, data
    data = y.recv(1024)
    data = loads(data)


def send_msg():
    global y
    y.sendall(dumps(' i was called and am new'))


visit_on_host()