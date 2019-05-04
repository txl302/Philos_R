import picamera
import picamera.array
from time import sleep
import cv2

camera = picamera.PiCamera()

camera.resolution = (640,480)
rawCapture = picamera.array.PiRGBArray(camera,size=(640,480))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
rectangleColor = (0,165,255) 

sleep(0.1)

for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
    image = frame.array

    cv2.flip(image, -1, image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    maxArea = 0  
    x = 0  
    y = 0  
    w = 0  
    h = 0

    for (_x,_y,_w,_h) in faces:

        if _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h
    if maxArea > 0:
        cv2.rectangle(image,(x,y),(x+w,y+h),rectangleColor,4)
        a = x+w/2
        b = y+h/2
            
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        cv2.putText(image, "x: {}, y: {}".format(a, b), (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
 
    cv2.imshow('img',image)
 
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

