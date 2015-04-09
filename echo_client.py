#!/usr/bin/env python

'''Echo me back!'''

import socket

host = 'michaelkilby.me'
port = 9999

rec_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rec_sock.connect((host,port))
rec_sock.send('Hello World, testing.')
data = rec_sock.recv(1024)
rec_sock.close()
print "I got a message! ", data
