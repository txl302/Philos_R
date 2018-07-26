import cv2
import socket

import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.183', 9999))

while True:
	data,addr = s.recvfrom(64000)

	data = numpy.fromstring(data,dtype='uint8') 

	print data

	image=cv2.imdecode(data,1)

	cv2.imshow('Taoge Niubi', image)
	if cv2.waitKey(10) == 27:
		break
s.close()
