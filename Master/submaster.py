import socket
import threading

table_robot = {}
table_function_p = {}
table_function_a = {}

s_r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_r.bind(('', 8013))
s_p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_p.bind(('',8014))
s_a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_a.bind(('',8015))

def listen_robot():
	global table_robot
	data, addr = s_r.recvfrom(1024)

	rob = data.split('|')

	if rob[0] == 'connect':
		robot_name = rob[1]
		print 'Robot %s is online now' %robot_name
		table_robot[robot_name] = rob[2]

	elif rob[0] == 'disconnect':
		robot_name = rob[1]
		print 'Robot %s disconnect from the server' %robot_name
		table_robot.pop(addr)

	elif rob[0] == 'request':
		robot_name = rob[1]
		request = rob[2]
		n = len(request)
		answer = []
		for i in range(n):
			answer = answer.append(table_function_p[request[n]])
		s.sendto(answer, addr)

def listen_function_p():
	global table_function_p
	data, addr = s_p.recvfrom(1024)
	func = data.split('|')
	if func[0] == 'connect':
		function_name = func[1]
		print 'Function %s is online now' %function_name
		table_function_p[function_name] = func[2]
	elif func[0] == 'disconnect':
		function_name = func[1]
		print 'Function %s disconnect from the server' %function_name
		table_function_p.pop[function_name] 
	else:
		print "unknown request"

def listen_function_a():
	global table_function_p
	data, addr = s_p.recvfrom(1024)
	func = data.split('|')
	if func[0] == 'connect':
		function_name = func[1]
		print 'Function %s is online now' %function_name
		table_function_p[function_name] = func[2]
	elif func[0] == 'disconnect':
		function_name = func[1]
		print 'Function %s disconnect from the server' %function_name
		table_function_p.pop[function_name] 
	else:
		print "unknown request"

def robot_thread():
	while True:
		listen_robot()

def function_thread():
	while True:
		listen_function()

def command():
	global table_robot
	global table_function_p
	while True:
		str = raw_input()
		if str == 'robot':
			print 'The number of connected robot: %s' %len(table_robot)
			print table_robot
		elif str == 'function':
			print 'The number of online function: %s' %len(table_function_p)
			print table_function_p
		elif str == 'command':
			print 'command'
		elif str == 'help':
			print('robot: check the status of all robots\
				\nfucntion: check the status of all functions')
		else:
			print 'enter "help" for more command'

def test():
	t_robot = threading.Thread(target = listen_robot, name = 'robot_loop')
	t_function = threading.Thread(target = listen_function, name = 'function_loop')
	t_command = threading.Thread(target = command, name = 'command_loop')
	t_function.start()
	t_robot.start()
	t_command.start()
	t_function.join()
	t_robot.join()
	t_command.join()

if __name__ == '__main__':
	test()