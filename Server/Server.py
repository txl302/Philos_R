import socket
import threading

table_robot = []
table_function = []

def listen_robot():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('127.0.0.1', 8013))

	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' %addr
	print 'Robot %s online' %data


def listen_function():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('127.0.0.1',8014))

	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' %addr
	print 'function %s online' %data

	table_function.append(data)


def robot_thread():

	while True:
		listen_robot()


def function_thread():

	while True:
		listen_function()

def command():

	global table_robot
	global table_function

	while True:
		str = raw_input()

		if str == 'robot':
			print 'The number of connected robot: %s' %len(table_robot)
			print table_robot

		if str == 'function':
			print 'The number of online function: %s' %len(table_function)
			print table_function

		if str == 'command':
			print 'command'

		if str == 'help':
			print 'robot'

		else:
			print 'enter "help" for more command'



def test():
	#t_robot = threading.Thread(target = listen_robot, name = 'robot_loop')
	t_function = threading.Thread(target = listen_function, name = 'function_loop')

	t_command = threading.Thread(target = command, name = 'command_loop')

	t_function.start()
	#t_robot.start()
	t_command.start()

	t_function.join()
	#t_robot.join()
	t_command.join()



if __name__ == '__main__':
	test()