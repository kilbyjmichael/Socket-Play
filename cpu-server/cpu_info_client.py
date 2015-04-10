#!/usr/bin/env python

'''Receives the server's CPU data'''

import socket

host = 'michaelkilby.me'
port = 9999

rec_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rec_sock.connect((host,port))
rec_sock.send('Send CPU')
data = rec_sock.recv(1024)
rec_sock.close()
print host + "'s CPU data:", data
