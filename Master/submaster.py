import socket
import threading

table_robot = {}
table_function = {}

def listen_robot():
	
	global table_robot

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', 8013))

	data, addr = s.recvfrom(1024)

	if data.find('connect') >= 0:
		robot_name = data[9:]
		print 'Robot %s is online now' %robot_name
		table_robot[addr] = robot_name
		s.sendto('comfirmed', addr)

	elif data.find('disconnect') >= 0:
		robot_name = data[12:]
		print 'Robot %s disconnect from the server' %robot_name
		table_robot.pop(addr)

	elif data.find('request') >= 0:

		request = data[9:]
		n = len(request)

		answer = []

		for i in range n:
			answer = answer.append(table_function[request[n]])

		s.sendto(answer, addr)


def listen_function():

	global table_function

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('',8014))

	data, addr = s.recvfrom(1024)

	if data.find('connect') >= 0:
		function_name = data[9:]
		print 'Function %s is online now' %fucntion_name
		table_function[fucntion_name] = addr
		s.sendto('comfirmed', addr)

	elif data.find('disconnect') >= 0:
		fucntion_name = data[12:]
		print 'Function %s disconnect from the server' %fucntion_name
		table_function.pop(function_name)


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

		elif str == 'function':
			print 'The number of online function: %s' %len(table_function)
			print table_function

		elif str == 'command':
			print 'command'

		elif str == 'help':
			print('robot: check the status of all robots\
				\nfucntion: check the status of all functions')
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