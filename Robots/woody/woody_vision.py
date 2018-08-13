import cv2
import numpy

cam1 = cv2.VideoCapture(1)

def cam():
	ret1, img1 = cam1.read()
	if img1 != []:
		print img1
		img1 = cv2.resize(img1,(320,240)) 
	result, imgencode = cv2.imencode('.jpg',img1) 
	return imgencode
	cv2.waitKey(10)

if __name__ == '__main__':
	cam()