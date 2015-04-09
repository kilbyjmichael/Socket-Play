#!/usr/bin/env python

'''Echo me!'''

import socket

host = 'michaelkilby.me'
port = 9999

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((host,port))
serv_sock.listen(5)
print "I'm listening...!"

while True:
        client, address = serv_sock.accept()
        data = client.recv(1024)
        if data:
            client.send(data)
            print "I got a message! ", data
        client.close()
