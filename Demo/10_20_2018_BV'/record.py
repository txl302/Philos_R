from gtts import gTTS
import time
import os

localtime = time.asctime(time.localtime(time.time()))

ttss = "It's" + str(localtime)
file_name = 'time.mp3'

tts = gTTS(text=ttss, lang='en')
tts.save(file_name)
os.system("mpg321 " + file_name)

