#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 8888)
print('connecting to {} port {}'.format(server_addr[0], server_addr[1]))
sock.connect(server_addr)

msg = input('=>=> ')

while msg != 'quit':

    sock.send(msg.encode()) # encode into byte string to send to server
    data = sock.recv(1024).decode() # decode the byte from server into string
    print('from server: ' + data)
    msg = input('=>=> ')

sock.close()
