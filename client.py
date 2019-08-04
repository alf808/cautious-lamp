#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)
print('connecting to {} port {}'.format(server_addr[0], server_addr[1]))
sock.connect(server_addr)

try:
    msg = b'repeating message'
    print(f'sending {msg}')
    sock.send(msg)

    received = 0
    expected = len(msg)

    while received < expected:
        data = sock.recv(4096)
        received += len(data)
        print(data)
finally:
    sock.close()