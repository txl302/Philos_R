
import socket

from gtts import gTTS
import os



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def hello():
    tts = gTTS(text='Warning! Chuan qi, is not working', lang='en')
    tts.save("good.mp3")
    #os.system("mpg321 good.mp3")

    f = open('good.mp3', 'rb')

    data = f.read()

    s.sendto(data, ('192.168.1.32', 8099))
    s.sendto(data, ('192.168.1.94', 8099))

    print data

    f.close()



if __name__ == '__main__':
	hello()

