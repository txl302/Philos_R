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
	while time_total < 60:
		pose = [random.uniform(1, 80), random.uniform(-10, 20)]
		woody_action.move_to([1,2], pose)
		time_p = random.uniform(1,5)
		time.sleep(time_p)
		time_total = time_total + time_p

def sing_a_song():
	d = os.listdir('/home/pi/Philos_R/Robots/Woody/songs/')
	song_name = d[random.randint(0, len(d)-1)]
	os.system('mplayer ' + '/home/pi/Philos_R/Robots/Woody/songs/' + song_name)
	time.sleep(5)

def self_speaking():
	d = os.listdir('/home/pi/Philos_R/Robots/Woody/self_speaking/')
	words_name = d[random.randint(0, len(d)-1)]
	os.system('mplayer ' + '/home/pi/Philos_R/Robots/Woody/self_speaking/' + words_name)
	time.sleep(5)

def motion_detection():
	pass

def idle():
	n = random.randint(1,100)
	print n
	if n < 10:
		sing_a_song()
	elif n < 20:
		self_speaking()
	else:
		look_around()

def main():
	while True:
		idle()

if __name__ == '__main__':
	main()
