import cv2
import numpy as np
import os
import time

import sys
from PIL import ImageTk
from PIL import Image

class Auto_motion():
    
    def __init__(self):
        
        # choose 14 stage training result as finial detection tool after analyzing with ROC curve
        vocal_cord_cascade=cv2.CascadeClassifier('cascade_14_stage5050.xml')
        video='/home/pi/intubot/test_videos/Vocal_Cords_in_Action_cut.mp4'
        cap=cv2.VideoCapture(video)


        # initialize the detected object coordinate 
        x=0
        y=0

        # initialize the compensation coordinate of tip
        x_compensation=0
        y_compensation=0

        # initialize the previous coordinate
        x_previous=0
        y_previous=0

        # the switch for first loop, if it is the first loop, turn 0; otherwise, turn 1.
        first_step=0

        servo1=11
        servo2=13
        STEP=15
        DIR=16

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(STEP,GPIO.OUT)
        GPIO.output(STEP,0)
        GPIO.setup(DIR,GPIO.OUT)

        GPIO.setup(servo1,GPIO.OUT)
        GPIO.setup(servo2,GPIO.OUT)


        # STEPPER MOTOR Global Variables
        LR_bending=7.5
        FB_bending=7.5

        # PWM FREQENCY SETTING
        pwm1=GPIO.PWM(servo1,50)
        pwm2=GPIO.PWM(servo2,50)
        
        # turn the servos on 
        #pwm1.start(FB_bending)
        #pwm2.start(LR_bending)

        # detect the object, returns true if video capturing has been initialized already
        while(cap.isOpened()):
            # grabs, decodes and returns the next video frame
            ret,frame=cap.read()
            if ret is True:
                gray_video=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            else:
                break
            # 58 to 60 is the best MinNeighbors for stage14
            vocal_cord=vocal_cord_cascade.detectMultiScale(frame,5,58)
            # compensate the tip motion to the previous x and y coordinates
            x_previous=x_previous + x_compensation
            y_previous=y_previous + y_compensation
            for (x,y,w,h) in vocal_cord:
                # if it is in the first loop, the change between the coordinates must be big. So exclude this scenario from the wrong detection 
                if (abs(x_previous-x)>60) or (abs(y_previous-y)>60):
                    if first_step==0:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                        x_previous=x
                        y_previous=y
                        first_step=1
                    # get rid of the coordinates that got great change compared to the previous one   
##                    else:
##                        print 'wrong detection excluded'
                        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                            
                # draw the box to point the rest of the detected object out
                else:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) # the image to draw, starting point, ending point, color, line thickness.
                    x_previous=x
                    y_previous=y

            cv2.imshow('vocal cord detection',frame)
            
            if cv2.waitKey(1) & 0xFF== ord('q'):
                break
        
        # close video file or capturing device
        cap.release()
        cv2.destroyWindow('vocal cord detection')
        GPIO.cleanup()
            

#Auto_motion()