import os
import time
import random

import woody_action
import woody_vision

def check_env():

	woody_action.move_to([1], [])
	time.sleep(2)
	woody_action.move_to([1], [])
	time.sleep(2)

	woody_action.move_to([2], [])
	time.sleep(2)

	woody_action.move_to([1], [])
	time.sleep(2)
	woody_action.move_to([1], [])
	time.sleep(2)

	woody_action.move_to([2], [])
	time.sleep(2)

def look_around():
	time_total = 0
	while time < 60:
		pose = [random.uniform(1, 100), random.uniform(1, 20)]
		woody_action.move_to([1,2], pose)
		time_p = random.uniform(1,5)
		time.sleep(time_p)
		time_total = time_total + time_p

def sing_a_song():
	d = os.listdir(os.getcwd() + '/songs/')

	song_name = d[random.randint(0, len(d)-1)]

	print d, len(d), song_name
	print('mplayer ' + os.getcwd() + '/songs/'+ song_name)
	os.system('mplayer ' + os.getcwd() + '/songs/'+ song_name)

def self_speaking():
	os.system('mplayer self_destruction.wav')
	time.sleep(5)

def motion_detection():
	pass


def idle():
	while True:
		n = random.randint(1,100)
		if n < 10:
			sing_a_song()
		elif n < 20:
			self_speaking()
		else:
			look_around()

def main():
	idle()

if __name__ == '__main__':
	main()