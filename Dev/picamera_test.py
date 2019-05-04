import picamera
import picamera.array
from time import sleep
import cv2

camera = picamera.PiCamera()

camera.resolution = (640,480)
rawCapture = picamera.array.PiRGBArray(camera,size=(640,480))

sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
    image = frame.array

    cv2.flip(image, -1, image)

    result, imgencode = cv2.imencode('.jpg',image)

    cv2.imshow('frame', image)
 
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
                                                                               
