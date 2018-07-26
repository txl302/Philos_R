import cv2
import socket
import numpy
import threading

import woody_vision

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

imgencode = woody_vision.cam()

def cam():

	while True:
		global imgencode
		imgencode = woody_vision.cam()

def send1():
	while True:
		s.sendto(imgencode, ('192.168.1.42', 9999))
	s.close()

def send2():
	while True:
		s.sendto(imgencode, ('192.168.1.115', 9999))
	s.close()

thread_c = threading.Thread(target = cam);
thread_c.start();	

thread_s1 = threading.Thread(target = send1);
thread_s1.start();

thread_s2 = threading.Thread(target = send2);
thread_s2.start();
