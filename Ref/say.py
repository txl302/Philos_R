# -*- coding: UTF-8 -*-
import pyttsx3

engine = pyttsx3.init()

print engine.getProperty("rate")
#print engine.getProperty("voices")
voices = engine.getProperty("voices")
engine.setProperty("rate", 150)


engine.setProperty("voice", 'english')

engine.say("chan qee zheng, is not working!")
engine.runAndWait()