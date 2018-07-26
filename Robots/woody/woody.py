import cv2
import socket
import numpy
import threading

cam1 = cv2.VideoCapture(0)
ret1, img1 = cam1.read()

if img1 != []:
	img1 = cv2.resize(img1,(320,240)) 

result, imgencode = cv2.imencode('.jpg',img1) 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def cam():

    global imgencode

	while True:

		ret1, img1 = cam1.read()

		if img1 != []:
			img1 = cv2.resize(img1,(320,240)) 

		result, imgencode = cv2.imencode('.jpg',img1) 

		print imgencode

		if cv2.waitKey(10) == 27:
			break
	cv2.destroyAllwindows()

def send1():
	while True
		s.sendto(imgencode, ('192.168.1.42', 9999))
	s.close()

def send2():
	while True:
		s.sendto(imgencode, ('192.168.1.235', 9999))
	s.close()

thread_c = threading.Thread(target = cam);
thread_c.start();	

thread_s1 = threading.Thread(target = send1);
thread_s1.start();

thread_s2 = threading.Thread(target = send2);
thread_s2.start();
