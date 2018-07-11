import pypot.dynamixel

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect():
	
	global s

	data = 'connect'
	 
	s.sendto(data, ('127.0.0.1', 8014))

	if s.recv(1024) == 'comfirmed':
		s.sendto('test', ('127.0.0.1', 8014))

def disconnect():

	global s

	data = 'disconnect'

	s.sendto(data, ('127.0.0.1', 8014))

	s.close()


def test():

	connect()

if __name__ == '__main__':
	test()