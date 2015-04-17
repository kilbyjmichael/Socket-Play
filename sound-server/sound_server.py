#!/usr/bin/env python

'''Listen to me!'''

import socket
import pyaudio
import sys
import struct

host = 'localhost'
port = 9999

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

# pack dem vibes
vibe_pack = struct.pack('%si' % len(frames), *frames)

# sockets

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((host,port))
serv_sock.listen(5)
print "I'm waiting to send the data...!"

while True:
        client, address = serv_sock.accept()
        while vibe_pack:
            sent = client.send(vibe_pack)
            if not sent:
                # The socket has disconnected if the send fails
                break
            vibe_pack = vibe_pack[sent:]
