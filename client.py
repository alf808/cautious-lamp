#!/usr/bin/python3
import socket
import sys

port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', port)
print('connecting to {} port {}'.format(server_addr[0], server_addr[1]))
sock.connect(server_addr)

odd_data = 'GET /index.html HTTP/1.1\r\nHost: google.com\r\n\r\n'
# encode into byte string to send to server
sock.send(odd_data.encode())

data = sock.recv(1024).decode() # decode the byte from server into string
print('from server: ' + data)

sock.close()
