
import socket

from gtts import gTTS
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ports = [('192.168.1.115', 9999), ('192.168.1.115', 9998)]
s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

def init():
	print 'visual function initialized'
	init_request = 'connect| visual|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8014))


def hello():
    tts = gTTS(text='Warning! Chuan qi, is not working', lang='en')
    tts.save("good.mp3")
    #os.system("mpg321 good.mp3")

    f = open('good.mp3', 'rb')

    data = f.read()

    s.sendto(data, ('192.168.1.32', 8099))
    s.sendto(data, ('192.168.1.94', 8099))

    print data

    f.close()



if __name__ == '__main__':
	hello()

