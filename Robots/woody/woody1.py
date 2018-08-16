import cv2
import socket
import numpy
import threading
import os

import woody_vision
import woody_action

rob_name = 'woody1'

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

imgencode = woody_vision.cam()

function_server = {}

def init_check():
	print 'self checking......'
	os.system("mplayer speaker_checking.wav")

	woody_action.init_check()

def init():
	print 'robot %s initialing......' %rob_name

	init_check()

	init_request = 'connect| ' + rob_name + '|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8013))
	print 'robot %s initialized' %rob_name

	os.system("mplayer check_successful.wav")

def request():
	global function_server
	print 'sending request to server'
	f_request = ['visual', 'audio', 'motion']
	send_request = 'connect| woody1|' + str_ports
	s.sendto(send_request, ('192.168.1.235', 8013))
	feedback = s.recvfrom(1024)
	for i in range(len(f_request)):
		function_server[f_request[i]] = feedback[i]

def cam():
	while True:
		global imgencode
		imgencode = woody_vision.cam()

def send():
	while True:
		s.sendto(imgencode, function_server['visual'])
	s.close()

def audio():
	pass

def move():
	woody_action.move_to()

def self_check():
	pass

def run():
	thread_c = threading.Thread(target = cam);
	thread_c.start();

	thread_s = threading.Thread(target = send);
	thread_s.start();

	thread_a = threading.Thread(target = audio)
	thread_a.start()

	thread_m = threading.Thread(target = move)
	thread_m.start()

def main():
	init()
	request()
	run()

if __name__ == '__main__':
	main()


