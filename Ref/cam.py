import cv2

cam1 = cv2.VideoCapture(0)

while True:

	ret1, img1 = cam1.read()

	cv2.imshow('Taoge Niubi', img1)

	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllwindows()
