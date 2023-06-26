import socket

host = '127.0.0.1'
port=4545

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.bind((host,port))
    s.listen()
    print('listening...')
    conn,addr=s.accept()
    with conn :
        print(f'connect to {addr}')
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.send(data)
