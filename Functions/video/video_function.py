import cv2
import socket
import threading
import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ports = [('192.168.1.115', 9999), ('192.168.1.115', 9998)]
s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

def init():
	print 'visual function initialized'
	init_request = 'connect| visual|' + str_ports
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

def reveice_play(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')
	image = cv2.imdecode(data, 1)
	image = cv2.resize(image, (640,480))
	cv2.imshow(sc, image)
	cv2.waitKey(10)

def play1():
	while True:
		reveice_play(s1, "Taoge Niubi 1")
	s1.close()

def play2():
	while True:
		reveice_play(s2, "Taoge Niubi 2")
	s2.close()

def main():
	#init()
	thread_c = threading.Thread(target = command)
	thread_c.start()
	thread_s1 = threading.Thread(target = play1);
	thread_s1.start();
	thread_s2 = threading.Thread(target = play2);
	thread_s2.start();

	thread_c.join()

if __name__ == '__main__':
	main()