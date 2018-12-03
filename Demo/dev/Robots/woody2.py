import cv2
import socket
import threading
import os
import time
import itertools

from random import randint

from Woody import woody_action
m_ids = [1,2,3,4,5,6,7,8,9,10,11,12]
speed = [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]

move1 = 0.0
move2 = 0.0

vision_server = ("192.168.1.87", 9901)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.1.237", 9901))

s_vision = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def camera_send():
    while True:
        imgencode = woody_vision.cam()
        s_vision.sendto(imgencode, vision_server)
        cv2.imshow('img', imgencode)

        
def reveice_move(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')
        move(m_ids, data, speed)



	
if __name__ == '__main__':
    receive_move(s)
