table_function = []
table_robot = []

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

	command()

if __name__ == '__main__':
	test()
