import speech_recognition as sr
from gtts import gTTS
import os

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("Hello!")
    tts = gTTS(text='Greeting protocal initiated', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    tts = gTTS(text='Hi, I am Pheelos. I am ready', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
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
