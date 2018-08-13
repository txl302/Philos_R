import cv2
import socket
import numpy
import threading

import woody_vision
import woody_action

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ports = [('192.168.1.115', 9999), ('192.168.1.115', 9998)]
s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

imgencode = woody_vision.cam()

def init():
	print 'robot woody1 initialized'
	init_request = 'connect| woody1|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8013))


def cam():
	while True:
		global imgencode
		imgencode = woody_vision.cam()

def send1():
	while True:
		s.sendto(imgencode, ('192.168.1.42', 9999))
	s.close()

def send2():
	while True:
		s.sendto(imgencode, ('192.168.1.115', 9999))
	s.close()

def move():
	woody_action.move_to()

def self_check():
	pass
	
def main():
	thread_c = threading.Thread(target = cam);
	thread_c.start();
	thread_s1 = threading.Thread(target = send1);
	thread_s1.start();
	thread_s2 = threading.Thread(target = send2);
	thread_s2.start();
	thread_m = threading.Thread(target = move)
	thread_m.start()

if __name__ == '__main__':
	main()


