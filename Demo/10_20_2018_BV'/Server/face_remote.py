import cv2
import socket

cap = cv2.VideoCapture(0)
width = 320
height = 240
cap.set(3,width);
cap.set(4,height);

s_v = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:

    ret, img = cap.read()

    result, imgencode = cv2.imencode('.jpg',img) 

    s_v.sendto(imgencode, ("192.168.1.87", 9901))

    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
