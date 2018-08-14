import pyaudio

import socket
import numpy

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                #output=True,
                frames_per_buffer=CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = stream.read(CHUNK)

    print data

    s.sendto(data, ('192.168.1.183', 9999))

stream.stop_stream()
stream.close()

p.terminate()

