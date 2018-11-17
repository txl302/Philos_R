import cv2
import socket
import threading
import os
import time
import itertools

from random import randint

from Woody import woody_action


move1 = 0.0
move2 = 0.0

vision_server = ("192.168.1.87", 9901)


s_vision = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def camera_send():
    while True:
        imgencode = woody_vision.cam()
        s_vision.sendto(imgencode, vision_server)
        cv2.imshow('img', imgencode)



	
if __name__ == '__main__':
	#run()
    vision()
