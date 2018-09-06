import cv2
import socket
import numpy
import threading
import os
import time
import getpass

from Woody import woody_vision
from Woody import woody_motion
from Woody import woody_embedded

rob_name = 'woody1'
user_name = getpass.getuser()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_v = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

se = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

imgencode = []

function_server = {}

visual_flag = 0
motion_flag = 0
audio_flag = 0

def init_check():

	global visual_flag
	global motion_flag
	global audio_flag

	print 'self checking......'

	try:
		imgencode = woody_vision.cam()
		print "camera ready"
	except:
		print "camera offline"

	woody_embedded.random_look()

	try:
		os.system("mplayer /home/"+user_name+"/Philos_R/Robots/Woody/speaker_checking.wav")
	except:
		pass
	time.sleep(2)

	try:
		from Woody import woody_action
		print "motion module detected"
		try:
			woody_action.init_check()
			print "motion unit ready"
		except:
			print "motion unit error"
	except:
		print "motion module offline"
	time.sleep(2)


	time.sleep(2)

def init():
	print 'robot %s initialing......' %rob_name

	init_check()

	init_request = 'connect| ' + rob_name + '|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8013))
	print 'robot %s initialized' %rob_name

	os.system("mplayer /home/"+user_name+"/Philos_R/Robots/Woody/check_successful.wav")

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

def v_send():
	while True:
		s_v.sendto(imgencode, function_server['visual'])
	s_v.close()

def audio():
	pass

def move():
	woody_action.move_to()

def self_check():
	pass

def run():
	thread_c = threading.Thread(target = cam);
	thread_c.start();

	thread_v_s = threading.Thread(target = v_send);
	thread_v_s.start();

	thread_a = threading.Thread(target = audio)
	thread_a.start()

	thread_m = threading.Thread(target = move)
	thread_m.start()

def test():
        pose = woody_motion.move_to_left(50, 50, 50)
        woody_action.move_to([3,4,5], pose)

def send_to_emotion():
	while True:
		se.sendto(imgencode, (192.168.1.115, 8011))
	se.close()

def main():
    #test()
	init()

	#request()
	#run()

	while True:
		woody_embedded.idle()
	
if __name__ == '__main__':
	main()