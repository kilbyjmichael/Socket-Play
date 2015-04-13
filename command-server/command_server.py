#!/usr/bin/env python

'''Takes python code and executes it.'''

import socket, subprocess

host = 'michaelkilby.me'
port = 9999

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((host,port))
serv_sock.listen(5)
print "I'm listening...!"

while True:
        client, address = serv_sock.accept()
        bashCommand = client.recv(512)
        if bashCommand:
            print "I got a command!", bashCommand
            process = subprocess.check_output(bashCommand, shell = True)
            client.send(process)
            print "Sent it back."
        client.close()
