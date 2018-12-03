import cv2
import socket
import threading
import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_t.bind(("192.168.1.130", 9901))

s.bind(("192.168.1.220", 9901))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
rectangleColor = (0,165,255)  

width = 320
height = 240


def reveice_play(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')
	img = cv2.imdecode(data, 1)
	#image = cv2.resize(image, (640,480))

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	print gray
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)


	for (x,y,w,h) in faces:

	    cv2.rectangle(img,(x,y),(x+w,y+h),rectangleColor,4)
	    a = x+w/2
	    b = y+h/2

	    if a>5 and b>5:
	        move1 = -85*(a-width/2)/width
	        move2 = 14.5*(b-height/2)/height
	cv2.imshow(sc, img)


	cv2.waitKey(10)

while True:
    reveice_play(s, "play")

    



