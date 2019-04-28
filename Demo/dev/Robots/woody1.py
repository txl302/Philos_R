import cv2
import socket
import threading
import os
import time
import itertools
import numpy as np
import json

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
		p = woody_action.get_present_position(m_ids)
		#m_pos = str(p)
		m_pos = json.dumps(p)
		print m_pos
		s.sendto(m_pos, ("192.168.1.237", 9901))



	
if __name__ == '__main__':
	run()
