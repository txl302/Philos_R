import cv2
import socket
import threading

import numpy

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1.bind(('192.168.1.115', 9999))
s2.bind(('192.168.1.115', 9998))

def reveice_play(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')

	image = cv2.imdecode(data, 1)

	image = cv2.resize(image, (640,480))

	cv2.imshow(sc, image)

	cv2.waitKey(10)

def play1():
	while True:
		reveice_play(s1, "Taoge Niubi 1")
	s1.close()

def play2():
	while True:
		reveice_play(s2, "Taoge Niubi 2")
	s2.close()

thread_s1 = threading.Thread(target = play1);
thread_s1.start();

thread_s2 = threading.Thread(target = play2);
thread_s2.start();
