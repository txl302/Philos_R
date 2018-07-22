import pyaudio

import socket

import numpy

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.1.183', 9999))

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                #input=True,
                output=True,
                frames_per_buffer=CHUNK)


while True:
    data,addr = s.recvfrom(1024)
    #data = numpy.fromstring(data,dtype='uint8')

    print data
    stream.write(data, CHUNK)


stream.stop_stream()
stream.close()

p.terminate()






