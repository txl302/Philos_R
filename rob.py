import cv2
import socket

import numpy

cam1 = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

	ret1, img1 = cam1.read()

	if img1 != []:

		img1 = cv2.resize(img1,(640,480)) 

	result, imgencode = cv2.imencode('.jpg',img1) 

	#data=cv2.imdecode(imgencode,1)

	print imgencode

	s.sendto(imgencode, ('192.168.1.183', 9999))
	s.sendto(imgencode, ('192.168.1.42', 9999))

	#cv2.imshow('Taoge Niubi', image)

	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllwindows()	

s.close()