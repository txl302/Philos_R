import socket;
import threading; 
import struct; 
import cv2 
import time 
import os 
import numpy 

import pypot.dynamixel


cam1 = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

	ret1, img1 = cam1.read()

	if img1 != []:

		img1 = cv2.resize(img1,(640,480)) 

	result, imgencode = cv2.imencode('.jpg',img1) 

	print imgencode

	s.sendto(imgencode, ('192.168.1.183', 9999))
	s.sendto(imgencode, ('192.168.1.42', 9999))

	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllwindows()	

s.close()

def connect():
	
	global s

	data = 'connect'
	 
	s.sendto(data, ('192.168.1.42', 8013))

	if s.recv(1024) == 'comfirmed':
		s.sendto('woody', ('192.168.1.42', 8013))

def disconnect():

	global s

	data = 'disconnect'

	s.sendto(data, ('192.168.1.42', 8013))

	s.close()


def test():

	connect()

if __name__ == '__main__':
	test()