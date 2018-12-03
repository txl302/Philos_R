import cv2
import socket
import threading
import os
import time
import itertools

from random import randint

from Woody import woody_action

m_ids = [1,2,3,4,5,6,7,8,9,10,11,12]

vision_server = ("192.168.1.87", 9901)


s_vision = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def camera_send():
    while True:
        imgencode = woody_vision.cam()
        s_vision.sendto(imgencode, vision_server)
        cv2.imshow('img', imgencode)

def run():
	while True:
		woody_action.get_present_position(m_ids)



	
if __name__ == '__main__':
	run()