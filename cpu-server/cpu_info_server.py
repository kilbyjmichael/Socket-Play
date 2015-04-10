#!/usr/bin/env python

'''Server that sends cpu info on request'''

import socket, psutil

host = 'michaelkilby.me'
port = 9999

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((host,port))
serv_sock.listen(5)
print "I'm listening...!"

while True:
        client, address = serv_sock.accept()
        data = client.recv(512)
        if "Send CPU" in data:
            cpu_percent = str(psutil.cpu_percent(interval = 1, percpu=True))
            client.send("CPU usage percent: " + cpu_percent)
            client.send(str(psutil.net_io_counters(pernic=True)))
            boot_time = str(psutil.boot_time())
            client.send("\n" + "Boottime: " + boot_time)
            client.send("\nDone!")
            print "Information Sent."
        client.close()
