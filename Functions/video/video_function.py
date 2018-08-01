import cv2
import socket

import numpy

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.bind(('192.168.1.115', 9999))
s2.bind(('192.168.1.115', 9998))

while True:
	data1,addr1 = s1.recvfrom(64000)

	data1 = numpy.fromstring(data1,dtype='uint8') 

	data2,addr2 = s2.recvfrom(64000)

	data2 = numpy.fromstring(data2,dtype='uint8') 

	#print data

	image1=cv2.imdecode(data1,1)
	image2=cv2.imdecode(data2,1)

	image1 = cv2.resize(image1, (640,480))
	image2 = cv2.resize(image2, (640,480))

	cv2.imshow('Taoge Niubi 1', image1)
	cv2.imshow('Taoge Niubi 2', image2)
	if cv2.waitKey(10) == 27:
		break
s.close()
