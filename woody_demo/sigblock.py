import speech_recognition as sr
from gtts import gTTS
import os

import re

import itertools
import numpy
import time
import serial
import threading

import woody_action
import woody_voice

r = sr.Recognizer()
m = sr.Microphone()

with m as source: r.adjust_for_ambient_noise(source)

tv1 = threading.Thread(target = woody_voice.hello, name = 'voice_loop')
ta1 = threading.Thread(target = woody_action.hello, name = 'action_loop')

tv2 = threading.Thread(target = woody_voice.intro, name = 'voice_loop')
ta2 = threading.Thread(target = woody_action.point_mid_right, name = 'action_loop')

tv3 = threading.Thread(target = woody_voice.consent, name = 'voice_loop')
ta3 = threading.Thread(target = woody_action.point_close_left, name = 'action_loop')

tv4 = threading.Thread(target = woody_voice.get_ready, name = 'voice_loop')
ta4 = threading.Thread(target = woody_action.point_far_right, name = 'action_loop')

tv5 = threading.Thread(target = woody_voice.are_you_ready, name = 'voice_loop')
ta5 = threading.Thread(target = woody_action.point_far_right, name = 'action_loop')

tv6 = threading.Thread(target = woody_voice.shape_matching, name = 'voice_loop')
ta6 = threading.Thread(target = woody_action.point_far_right, name = 'action_loop')


tv1.start()
ta1.start()
tv1.join()
ta1.join()

tv2.start()
ta2.start()
tv2.join()
ta2.join()

tv3.start()
ta3.start()
tv3.join()
ta3.join()

tv4.start()
ta4.start()
tv4.join()
ta4.join()

tv5.start()
#ta5.start()
tv5.join()
#ta5.join()

value = 0



while value == 0:
    #print("Say something!")
    with m as source: audio = r.listen(source)
    #print("Got it! Now to recognize it...")
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            #print(u"You said {}".format(value).encode("utf-8"))
            print(value)

            #print("{}".format(value).encode("utf-8"))
            tts = gTTS(text='Great!', lang='en')
            tts.save("good.mp3")
            os.system("mpg321 good.mp3")
        else:  # this version of Python uses unicode for strings (Python 3+)
            print("You said {}".format(value))
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
        tts = gTTS(text='Sorry, I dont understand', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))



if value:
	tv6.start()
	ta6.start()
	tv6.join()
	ta6.join()


