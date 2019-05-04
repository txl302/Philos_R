import picamera
import picamera.array
from time import sleep
import cv2

import socket

camera = picamera.PiCamera()

#camera.resolution = (1024,768)

#rawCapture = picamera.array.PiRGBArray(camera,size=(1024,768))

camera.resolution = (320,240)
rawCapture = picamera.array.PiRGBArray(camera,size=(320,240))

s_v = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
    image = frame.array

    result, imgencode = cv2.imencode('.jpg',image)

    cv2.imshow('frame', image)

    s_v.sendto(imgencode, ("192.168.1.99", 9901))
 
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
