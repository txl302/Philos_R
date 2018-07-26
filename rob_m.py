import cv2
import socket

import numpy

cam1 = cv2.VideoCapture(0)

ret1, img1 = cam1.read()

if img1 != []:

	img1 = cv2.resize(img1,(320,240)) 

result, imgencode = cv2.imencode('.jpg',img1) 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def cam():

	while True:

		ret1, img1 = cam1.read()

		if img1 != []:

			img1 = cv2.resize(img1,(320,240)) 

		result, imgencode = cv2.imencode('.jpg',img1) 

		#data=cv2.imdecode(imgencode,1)

		print imgencode

		#cv2.imshow('Taoge Niubi', image)

		if cv2.waitKey(10) == 27:
			break
	cv2.destroyAllwindows()	

	s.close()

def send1():

	s.sendto(imgencode, ('192.168.1.42', 9999))

thread_c = threading.Thread(target = cam);
thread_c.start();	

thread_s1 = threading.Thread(target = send1);
thread_s1.start();

thread_c.join()
thread_s1.join()
