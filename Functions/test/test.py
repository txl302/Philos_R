import cv2
import socket
import numpy
from gtts import gTTS
import os

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.bind(('192.168.1.235', 9998))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

count = 0

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

	
def fun_request():
	request = ['visual', 'audio', '']

if __name__ == '__main__':

	data,addr = s1.recvfrom(64000)

	data = numpy.fromstring(data,dtype='uint8') 

	bg = cv2.imdecode(data,1)

	bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

	det = numpy.zeros(bg.shape, numpy.uint8)

	while True:
		data,addr = s1.recvfrom(64000)

		data = numpy.fromstring(data,dtype='uint8') 

		image = cv2.imdecode(data,1)

		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		det = cv2.absdiff(image, bg)

		for i in range (1,319,20):
			for j in range (1,219,20):
				if (det.item(j,i)>10):
					count = count + 1
		print count
		if(count > 12):
			tts = gTTS(text='Warning! Chuan qi, is not working', lang='en')
			tts.save("good.mp3")
			#os.system("mpg321 good.mp3")

			f = open('good.mp3', 'rb')

			data = f.read()

			s.sendto(data, ('192.168.1.32', 8099))
			s.sendto(data, ('192.168.1.94', 8099))

			f.close()

		count = 0

		cv2.imshow('Taoge Niubi', image)

		if cv2.waitKey(10) == 27:
			break
	s.close()
