import socket,time,sys,pickle

print('welcome to chat room')
print('initialising...')

time.sleep(2)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
port=4444
s.bind((host,port))
print(f'{host} {ip}')
name = input('Enter your name : ')
s.listen(2)
print('Waiting for incoming connection')
conn,addr=s.accept()
print(f'connection from {addr[0]} {addr[1]}')
c_name=conn.recv(1024)
c_name=pickle.loads(c_name)
print(f'{c_name} connected to chat room ')
conn.send(pickle.dumps(name))

while True:
    msg=str(input('Me : '))
    conn.send(pickle.dumps(msg))
    msg=conn.recv(1024)
    msg=pickle.loads(msg)
    print(f'{c_name} : {msg}')
