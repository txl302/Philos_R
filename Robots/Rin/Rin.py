import cv2
import socket

import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.32', 8099))


while True:
	data,addr = s.recvfrom(64000)

	f = open('good.mp3', 'wb')

	f.write(data)

	f.close()

	os.system("mpg321 good.mp3")

s.close()
