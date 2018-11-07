import cv2
import socket
import threading
import os
import time
import itertools

#import speech_recognition as sr
#from gtts import gTTS
from random import randint
#import pypot.dynamixel

#from Woody import woody_action
#from Woody import woody_motion

cap = cv2.VideoCapture(0)
width = 320
height = 240
cap.set(3,width);
cap.set(4,height);

move1 = 0.0
move2 = 0.0


s_vision = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s_nm = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#s_nm.bind(("192.168.1.143", 9902))

def camera_send():

    ret, img = cap.read()
    result, imgencode = cv2.imencode('.jpg',img) 

    s_vision.sendto(imgencode, ("192.168.1.220", 9901))

    cv2.imshow('img',img)

def vision():
    while True:
        if (flag == 0):
            camera_send()
            k = cv2.waitKey(20) & 0xff
            if k == 27:
                break

def neck_move():
    print flag


    while True:
        if (flag == 0):

            data,addr = s.recvfrom(64000)

            a = data.split()

            move_1 = double(a[0])
            move_2 = double(a[1])



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


#r = sr.Recognizer()
#m = sr.Microphone()

init = {}

flag = 0
value = 0


# print("A moment of silence, please...")
# with m as source: r.adjust_for_ambient_noise(source)
# print("Set minimum energy threshold to {}".format(r.energy_threshold))
# print("Hello!")


def voice_recog():
    global flag
    global value
    while True:
        if (flag == 0):
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                value = r.recognize_google(audio)
                if str is bytes:
                    print(value)
                    flag = 1
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

        thread_v.start()
        #thread_neck.start()

        #thread_r.start()
        #thread_a.start()
        #thread_m.start()


	
if __name__ == '__main__':
	#run()
    vision()
