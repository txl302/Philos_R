import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect():
	
	global s

	data = 'test function'
	 
	s.sendto(data, ('127.0.0.1', 8014))

def disconnect():

	global s

	data = 'disconnect'

	s.sendto(data, ('127.0.0.1', 8014))

	s.close()

def command():
	global table_robot
	global table_function

	while True:
		str = raw_input()

		if str == 'connect':
			connect()

		if str == 'disconnect':
			disconnect()

		if str == 'command':
			print 'command'

		if str == 'help':
			print 'robot'

		else:
			print 'enter "help" for more command'
	

def test():

	t_command = threading.Thread(target = command, name = 'command_loop')

	t_command.start()

	t_command.join()

if __name__ == '__main__':
	test()