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
	coommand()

if __name__ == '__main__':
	test()
