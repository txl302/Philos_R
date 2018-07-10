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

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

r = sr.Recognizer()
m = sr.Microphone()

with m as source: r.adjust_for_ambient_noise(source)

tv1 = threading.Thread(target = woody_voice.welcome, name = 'voice_loop')
ta1 = threading.Thread(target = woody_action.hello, name = 'action_loop')




tv1.start()
ta1.start()
tv1.join()
ta1.join()



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

            value = "Hi, " + value + "  can you give me a hug?"

            #print("{}".format(value).encode("utf-8"))
            tts = gTTS(text = value, lang='en')
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


woody_action.hugging()



tts = gTTS(text='Thank you. Humans are very cool, they are kind, friendly and creative.        as I been told.', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

try:
    while True:
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
                response = chatbot.get_response(value)
                print(response)
                #print("{}".format(value).encode("utf-8"))
                tts = gTTS(text=str(response), lang='en')
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
except KeyboardInterrupt:
    pass
