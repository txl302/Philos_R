import socket

import threading
import numpy

from gtts import gTTS
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ports = []

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

lo_addr = get_host_ip()

av_ports = [9998, 9999]

for i in range(len(av_ports)):
   ports.append((lo_addr, av_ports[i]))
   
s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

def init():
	print 'Audio function initialized'
	init_request = 'connect| audi0|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8014))

def command():
   while True:
      str = raw_input()
      if str == 'connect':
         request = 'connect| audio|' + str_ports
         s.sendto(request, ('192.168.1.235', 8014))
      elif str == 'disconnect':  
         request = 'disconnect| motion|' + str_ports
         s.sendto(request, ('192.168.1.235', 8014))
      elif str == 'help':
         print 'help'
      else:
         print 'enter "help" for more command'

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

def main():
    init()
    thread_c = threading.Thread(target = command)
    thread_c.start()

if __name__ == '__main__':
    main()