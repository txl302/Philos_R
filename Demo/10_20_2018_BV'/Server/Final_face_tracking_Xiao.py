import numpy as np
import cv2
import itertools
import numpy
import time
import serial

import pypot.dynamixel
import time
import RPi.GPIO as GPIO

ports = pypot.dynamixel.get_available_ports()
print('available ports:', ports)  

if not ports:
    raise IOError('No port available.') 

port = ports[0]
print('Using the first on the list', port)

dxl_io = pypot.dynamixel.DxlIO(port)
print('Connected!')

found_ids = dxl_io.scan()
print('Found ids:', found_ids)

if len(found_ids) < 2:
    raise IOError('You should connect at least two motors on the bus for this test.')

ids = found_ids[:]
dxl_io.enable_torque(ids)
speed = dict(zip(ids, itertools.repeat(20)))
dxl_io.set_moving_speed(speed)
dxl_io.set_moving_speed(dict(zip([1,2], itertools.repeat(55))))
dxl_io.set_moving_speed(dict(zip([3,8], itertools.repeat(25))))
start_pose=[ -55.28, -9.53, 45.6, 30.06, -7.48, 49.12, -46.77, -44.13, -27.13, 8.94, -37.39, 50.0]
dxl_io.set_goal_position(dict(zip(ids, start_pose)))
time.sleep(1.5)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
rectangleColor = (0,165,255)  

cap = cv2.VideoCapture(0)
width = 320
height = 240
cap.set(3,width);
cap.set(4,height);


while 1:
    dxl_io.enable_torque(ids)
    speed = dict(zip(ids, itertools.repeat(20)))
    dxl_io.set_moving_speed(speed)
    dxl_io.set_moving_speed(dict(zip([1,2], itertools.repeat(20))))
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
        cv2.rectangle(img,(x,y),(x+w,y+h),rectangleColor,4)
        a = x+w/2
        b = y+h/2
        print ('face x coord',a)
        print ('face y coord',b)
        p_1 = dxl_io.get_present_position((1,))
        p_2 = dxl_io.get_present_position((2,))
        print(p_1)
        p_1 = p_1[0]
        p_2 = p_2[0]
        if a>5 and b>5:
            p_1 = dxl_io.get_present_position((1,))
            p_2 = dxl_io.get_present_position((2,))
            p_1 = p_1[0]
            p_2 = p_2[0]
            print('p1',p_1)
            print('p2',p_2)
##            if a<90 or a>220:
            if (-90<p_1<-5 and -10<p_2<5):
                move_1 = -85*(a-width/2)/width
                move_2 = 14.5*(b-height/2)/height
                c_move_1 = p_1+0.4 *move_1
                c_move_2 = p_2+0.4*move_2
                if (-90<c_move_1<-5 and -10<c_move_2<5):
                    dxl_io.set_goal_position(dict(zip([1], [c_move_1])))
                    dxl_io.set_goal_position(dict(zip([2], [c_move_2])))
                    time.sleep(0.2)
##                        p_11 = dxl_io.get_present_position((1,))
##                        p_22 = dxl_io.get_present_position((2,))
##                        p_11 = p_11[0]
##                        p_22 = p_22[0]
##                        print('p11',p_11-c_move_1)
##                        print('p22',p_22-c_move_2)
                        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.putText(img, "x: {}, y: {}".format(a, b), (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 5)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
