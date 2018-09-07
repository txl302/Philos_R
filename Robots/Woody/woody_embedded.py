import os
import time
import random

import woody_vision

try:
	import woody_action
except:
	pass

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

def random_look():
	pose = [random.uniform(1, 80), random.uniform(-10, 20)]
	woody_action.move_to([1,2], pose)

def look_around():
	time_total = 0
	while time_total < 60:
		time_p = random.uniform(1,5)
		random_look()
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

["anger",  "disgust" ,"fear","happiness", "neutral", "sadness", "surprise"]
ids = [1,2,3,4,5,6,7,8,9,10,11,12]
ems = '/home/pi/Philos_R/Robots/Woody/embedded_speech/'

def anger():
	anger_pose1 = []
	anger_pose2 = []
	woody_action.move_to(ids, anger_pose1)
	time.sleep(1)
	woody_action.move_to(ids, anger_pose2)
	os.system('mplayer ' + d + 'anger.mp3')

def disgust():
	disgust_pose = []
	woody_action.move_to(ids, disgust_pose)
	os.system('mplayer ' + d + 'disgust.mp3')

def fear():
	fear_pose = []
	woody_action.move_to(ids, fear_pose)
	os.system('mplayer ' + d + 'fear.mp3')

def happiness():
	disgust_pose = []
	woody_action.move_to(ids, hapiness_pose)
	os.system('mplayer ' + d + 'happiness.mp3')

def neutral():
	disgust_pose = []
	woody_action.move_to(ids, neutral_pose)
	os.system('mplayer ' + d + 'neutral.mp3')

def sadness():
	disgust_pose = []
	woody_action.move_to(ids, sadness_pose)
	os.system('mplayer ' + d + 'sadness.mp3')

def surprise():
	disgust_pose = []
	woody_action.move_to(ids, surprise_pose)
	os.system('mplayer ' + d + 'surprise.mp3')

def main():
	while True:
		idle()

if __name__ == '__main__':
	main()
