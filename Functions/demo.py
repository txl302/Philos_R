import cv2
import socket
import threading
import numpy

from common import functional

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_e = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ports = []

master = {}

def search_master():

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

	PORT = 1060

	s.bind(('', PORT))

	while master == {}:
		data, address = s.recvfrom(65535)
    	master[address] = data
    	print data, address
    	print master

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

lo_addr = get_local_ip()

av_ports = [9991, 9992, 9993] #Emotion, Motion, Audio
for i in range(len(av_ports)):
   ports.append((lo_addr, av_ports[i]))

rob_ports = [9901, 9902, 9903] #Woody1, Woody2, Woody3
for i in range(len(av_ports)):
   ports.append((lo_addr, rob_ports[i]))

s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

def init():
	print 'visual function initialized'
	init_request = 'connect| visual| motion| audio|' + str_ports
	s.sendto(init_request, ('192.168.1.235', 8014))

def command():
	while True:
		str = raw_input()
		if str == 'connect':
			request = 'connect| visual|' + str_ports
			s.sendto(request, ('192.168.1.235', 8014))
			print 's'
		elif str == 'disconnect':	
			request = 'disconnect| visual|' + str_ports
			s.sendto(request, ('192.168.1.235', 8014))
		elif str == 'help':
			print 'help'
		else:
			print 'enter "help" for more command'

# def reveice_play(s,sc):
# 	data,addr = s.recvfrom(64000)
# 	data = numpy.fromstring(data, dtype = 'uint8')
# 	image = cv2.imdecode(data, 1)
# 	image = cv2.resize(image, (640,480))
# 	cv2.imshow(sc, image)
# 	cv2.waitKey(10)

# def play1():
# 	while True:
# 		reveice_play(s1, "Taoge Niubi 1")
# 	s1.close()

# def play2():
# 	while True:
# 		reveice_play(s2, "Taoge Niubi 2")
# 	s2.close()

def run():
	s_e.bind()
	s_e.recvfrom(64000)


def main():
	init()
	thread_c = threading.Thread(target = command)
	thread_c.start()
	thread_s1 = threading.Thread(target = play1);
	thread_s1.start();
	thread_s2 = threading.Thread(target = play2);
	thread_s2.start();

	thread_c.join()

def test():
	search_master()



if __name__ == '__main__':
	run()