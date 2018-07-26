import cv2
import socket

import numpy

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.bind(('192.168.1.32', 8099))

while True:
	data,addr = s1.recvfrom(64000)

	#print data

	image1=cv2.imdecode(data1,1)
	image2=cv2.imdecode(data2,1)

	cv2.imshow('Taoge Niubi 1', image1)
	cv2.imshow('Taoge Niubi 2', image2)
	if cv2.waitKey(10) == 27:
		break
s.close()
