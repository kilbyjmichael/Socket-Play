#!/usr/bin/env python

'''Sends and receives python command data.'''

import socket

host = 'michaelkilby.me'
port = 9999

rec_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rec_sock.connect((host,port))
bashCommand = raw_input("Enter bash command: ")
rec_sock.send(bashCommand)
data = rec_sock.recv(2048)
rec_sock.close()
print "I sent a command!\n"
print data
