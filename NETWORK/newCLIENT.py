import socket
host='127.0.0.1'
port=4545

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((host,port)),print('listening....')
    s.sendall(b'hey my server')
    data=s.recv(1024)
print(f'server message received {data}')
