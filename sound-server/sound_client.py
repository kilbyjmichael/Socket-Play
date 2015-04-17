#!/usr/bin/env python

'''I'll hear you!'''

import socket
import pyaudio

host = 'localhost'
port = 9999

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

rec_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rec_sock.connect((host,port))
# rec_sock.send('Hello, send me the music!')

music = rec_sock.recv(5120)
buffer = ''
while len(buffer) < 5120:
    chunk = rec_sock.recv(5120 - len(buffer))
    if not chunk:
        # If we can't receive any data, then the socket has died
        break
    buffer += chunk
print "I got a message!"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

stream.write(music, CHUNK)
    
print("Done playing!")

stream.stop_stream()
stream.close()

p.terminate()
