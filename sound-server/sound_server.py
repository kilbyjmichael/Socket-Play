#!/usr/bin/env python

'''Listen to me!'''

import socket
import pyaudio
import sys

host = '10.134.98.188'
port = 9998

# audio record

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Sing for me baby!")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("I got all your beautiful vibes.")

# sockets

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((host,port))
serv_sock.listen(5)
print "I'm waiting to send the data...!"

while True:
        client, address = serv_sock.accept()
        data = client.recv(1024)
        if data:
            client.send(frames)
            print "I sent the data!"
            client.close()
