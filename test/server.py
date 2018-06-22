import socket
import threading

def listen_robot():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('127.0.0.1'), 9999)

	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' %addr
	print 'Robot %s online' %data

	return 0

def listen_function():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('127.0.0.1'), 9999)

	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' %addr
	print 'function %s online' %data

	return 0

def robot_thread():

	while True:
		listen_robot()


def function_thread():

	while True:
		listen_function()


def test():
	t_robot = threading.Thread(target = listen_robot, name = 'robot_loop')
	t_function = threading.Thread(target = listen_function, name = 'function_loop')


if __name__ == '__main__':
	test()