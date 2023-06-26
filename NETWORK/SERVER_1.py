import socket
import sys
import selectors
import types

sel = selectors.DefaultSelector()

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f'listening on {(host, port)}')
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
print(type(selectors.EVENT_READ))