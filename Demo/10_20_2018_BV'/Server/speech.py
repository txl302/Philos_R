import speech_recognition as sr
from gtts import gTTS
import time
import os

r = sr.Recognizer()
m = sr.Microphone()

init = {}

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Hello!")

    os.system("mpg321 initiation.mp3")

    while True:
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            value = r.recognize_google(audio)

            if str is bytes:

                print(value)

                if value.find("hi") >= 0:
                    os.system("mpg321 hello.mp3")

                elif value.find("hello") >= 0:
                    os.system("mpg321 hi.mp3")

                elif value.find("name") >= 0:
                    os.system("mpg321 myname.mp3")

                elif value.find("how are you") >= 0:
                    os.system("mpg321 imgoodhowru.mp3")

                elif value.find("whether") >= 0:
                    os.system("mpg321 idkino.mp3")

                elif value.find("good afternoon") >= 0:
                    os.system("mpg321 goodafternoon.mp3")

                elif value.find("time") >= 0:
                    localtime = time.asctime(time.localtime(time.time()))
                    ttss = "It's" + str(localtime)
                    file_name = 'time.mp3'
                    tts = gTTS(text=ttss, lang='en')
                    tts.save(file_name)
                    os.system("mpg321 " + file_name)

                elif value.find("old") >= 0:
                    os.system("mpg321 justborn.mp3")

                else:
                    os.system("mpg321 idu.mp3")

            else:
                print("You said {}".format(value))

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")

            os.system("mpg321 idu.mp3")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
