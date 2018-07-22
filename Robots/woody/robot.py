import socket;
import threading; 
import struct; 
import cv2 
import time 
import os 
import numpy 
class webCamera:

	def run():

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

class lis:

	

def main(): 
	cam = webCamera()
	cam.run()

if __name__ == "__main__":
	main();