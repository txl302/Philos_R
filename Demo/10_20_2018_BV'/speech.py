import speech_recognition as sr
from gtts import gTTS
import time
import os

r = sr.Recognizer()
m = sr.Microphone()

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
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                #print(u"You said {}".format(value).encode("utf-8"))
                print(value)

                if value == "hi":
                    os.system("mpg321 hello.mp3")

                elif value == "hello":
                    os.system("mpg321 hi.mp3")

                elif value == "what's your name":
                    os.system("mpg321 myname.mp3")

                elif value == "how are you":
                    os.system("mpg321 imgoodhowru.mp3")

                elif value == "how is the weather today":
                    os.system("mpg321 idkino.mp3")

                elif value == "good afternoon":
                    os.system("mpg321 goodafternoon.mp3")

                elif value == "what time is it":
                    localtime = time.asctime(time.localtime(time.time()))
                    ttss = "It's" + str(localtime)
                    file_name = 'time.mp3'
                    tts = gTTS(text=ttss, lang='en')
                    tts.save(file_name)
                    os.system("mpg321 " + file_name)

                elif value == "how old are you":
                    os.system("mpg321 justborn.mp3")

                else:
                    os.system("mpg321 idu.mp3")




            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")

            os.system("mpg321 idu.mp3")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
