import cv2
import socket
import numpy
import threading
import os
import time

from Woody import woody_action
from Woody import woody_motion


import speech_recognition as sr
from gtts import gTTS

import numpy as np

import itertools

import pypot.dynamixel

import threading
from random import randint

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
rectangleColor = (0,165,255)  

cap = cv2.VideoCapture(0)
width = 320
height = 240
cap.set(3,width);
cap.set(4,height);



move1 = 0.0
move2 = 0.0

def camera():
    global move1
    global move2
    ret, img = cap.read()
    #print img

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

        if a>5 and b>5:
            move1 = -85*(a-width/2)/width
            move2 = 14.5*(b-height/2)/height
            #print move1, move2
            return (move1, move2)
            
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        #cv2.putText(img, "x: {}, y: {}".format(a, b), (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        #1, (0, 0, 255), 5)
 
    #cv2.imshow('img',img)

def vision():

        while True:
                if (flag == 0):
                        camera()
                        k = cv2.waitKey(20) & 0xff
                        if k == 27:
                                break
                        
                #time.sleep(0.3)

                


def neck_move():
    global move1
    global move2
    print flag
    while True:
                #print flag
                if (flag == 0):
                    move_1 = move1
                    move_2 = move2
                    #print move_1, move_2
                    #p_1 = dxl_io.get_present_position((1,))
                    #p_2 = dxl_io.get_present_position((2,))
                    p_1 = woody_action.get_present_position((1,))
                    p_2 = woody_action.get_present_position((2,))
                    p_1 = p_1[0]
                    p_2 = p_2[0]
                    if (-90<p_1<-5 and -10<p_2<5):
                            c_move_1 = p_1+0.4 *move_1
                            c_move_2 = p_2+0.4*move_2
                            if (-90<c_move_1<-5 and -10<c_move_2<5):
                                    woody_action.move_to([1,2], [c_move_1, c_move_2])
                time.sleep(0.3)



r = sr.Recognizer()
m = sr.Microphone()

init = {}

flag = 0
value = 0


print("A moment of silence, please...")
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
print("Hello!")




def fake():
    global flag
    global value
    cumu = 0
    s = ['hi', 'hello', 'are you', 'afternoon', 'old', 'weather', 'hug', 'dance', 'music']
    i = 0
    while True:
        print flag, 'fake'

        if (flag == 0):
            cumu = cumu + 1
            print cumu
            if cumu == 40:
                    value = s[i]
                    print value
                    flag = 1
                    cumu = 0
                    if i<=7:
                        i = i + 1
                    else:
                        i = 0
        time.sleep(0.3)



def voice_recog():
        global flag
        global value

        while True:
                #print flag
                if (flag == 0):
                            
                        with m as source: audio = r.listen(source)
                        print("Got it! Now to recognize it...")
                        try:
                            value = r.recognize_google(audio)

                            if str is bytes:

                                print(value)

                                flag = 1
                                #print flag

                            else:
                                print("You said {}".format(value))

                        except sr.UnknownValueError:
                            print("Oops! Didn't catch that")

                            os.system("mpg321 idu.mp3")

                time.sleep(30)
                        

def audio():
        global flag
        while True:
                
                if (flag == 1):
                        print value, bool(value)
                        if value:
                                print 'ok'

                                if value.find("hi") >= 0:
                                    os.system("mplayer voice/intro.mp3")
                                    flag = 0

                                elif value.find("hello") >= 0:
                                    os.system("mplayer voice/hello.mp3")
                                    flag = 0

                                elif value.find("old") >= 0:
                                    os.system("mplayer voice/how\ old\ are\ you.mp3")
                                    flag = 0  

                                elif value.find("are you") >= 0:
                                    os.system("mplayer voice/how\ are\ you.mp3")
                                    flag = 0

                                elif value.find("afternoon") >= 0:
                                    os.system("mplayer voice/good\ afternnon.mp3")
                                    flag = 0

                                elif value.find("hug") >= 0:
                                    os.system("mplayer voice/hug.mp3")
                                    flag = 0

                                elif value.find("sad") >= 0:
                                    os.system("mplayer voice/sad.mp3")
                                    flag = 0
                                    
                                elif value.find("dance") >= 0:
                                    os.system("mplayer voice/dance.m4a")
                                    flag = 0

                                elif value.find("weather") >= 0:
                                    os.system("mplayer voice/weather.mp3")
                                    flag = 0

                                elif value.find("music") >= 0:
                                    os.system("mplayer voice/mozart.mp3")
                                    flag = 0

                                else:
                                    os.system("mplayer voice/sorry.mp3")
                                    flag = 0
                time.sleep(0.3)
        

def motion():
        global flag
        while True:
                if (flag == 1):
                        print value, bool(value)
                        if value:
                                print 'ok'

                                if value.find("hi") >= 0:
                                    woody_action.hello()

                                elif value.find("hello") >= 0:
                                    woody_action.hello()

                                elif value.find("afternoon") >= 0:
                                    woody_action.thank_you()

                                elif value.find("hug") >= 0:
                                    woody_action.hugging()

                                elif value.find("sad") >= 0:
                                    woody_action.crying()

                                elif value.find("dance") >= 0:
                                    woody_action.dance2()

                                elif value.find("music") >= 0:
                                    woody_action.dance2()
                                    woody_action.dance3()
                                    woody_action.dance2()

                time.sleep(0.3)
                
def run():
        thread_neck = threading.Thread(target = neck_move)
        thread_v = threading.Thread(target = vision)
    
        

        thread_r = threading.Thread(target = voice_recog)
        
        thread_a = threading.Thread(target = audio)

        thread_m = threading.Thread(target = motion)

        thread_f = threading.Thread(target = fake)

        thread_v.start()
        thread_neck.start()

        thread_f.start()

        thread_r.start()
        thread_a.start()
        thread_m.start()


	
if __name__ == '__main__':
	run()
        #vision()
