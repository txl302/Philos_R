import cv2
import socket
import threading
import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("192.168.1.87", 9901))

def reveice_play(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')
	image = cv2.imdecode(data, 1)
	image = cv2.resize(image, (640,480))
	cv2.imshow(sc, image)
	cv2.waitKey(10)

while True:
    reveice_play(s, "play")

    
