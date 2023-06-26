import socket,time,sys,pickle

print('welcome to chat room ')
print('initialising...' )

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
chost=socket.gethostname()
ip = socket.gethostbyname(chost)
print(f'{chost} {ip}')
host=str(input('Enter teh server name '))
name=str(input('Enter your name '))
port = 4444
print(f'trying to connect to srver {host}')
time.sleep(2)
s.connect((host,port))

print('Connection established')

s.send(pickle.dumps(name))
s_name= s.recv(1024)
s_name=pickle.loads(s_name)
print(f'{s_name} connected the teh chat room')

while True:
    msg = s.recv(1024)
    msg=pickle.loads(msg)
    print(f'{s_name} : {msg}')
    msg=input(str('Me :'))
    s.send(pickle.dumps(msg))

