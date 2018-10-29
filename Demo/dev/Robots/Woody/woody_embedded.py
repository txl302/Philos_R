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

starting_pose = [-55.28, -9.53, 45.6, 30.06, -7.48, 49.12, -46.77, -44.13, -27.13, 8.94, -37.39, 50.0]

def anger_disgust():

	woody_action.move_to([3], [0])
	time.sleep(1)
	woody_action.move_to([4,8], [-6.01, -29.47])
	time.sleep(1)
	woody_action.move_to([9], [-2.2])
	time.sleep(1)
	woody_action.move_to([9], [-27.13])
	time.sleep(1)
	woody_action.move_to([4,8], [30.06, -44.13])
	time.sleep(1)
	woody_action.move_to([3], [32.7])
	time.sleep(1)
	woody_action.move_to(ids, starting_pose)

	#os.system('mplayer ' + d + 'anger.mp3')


def fear_surprise():
	woody_action.move_to([3,8], [-59.09, 56.74])
	time.sleep(1)
	woody_action.move_to([4,9], [95.45, -93.7])
	time.sleep(1)
	woody_action.move_to([4,9], [30.06, -27.13])
	time.sleep(1)
	woody_action.move_to([3,8], [32.7, -32.11])
	time.sleep(1)
	woody_action.move_to(ids, starting_pose)

	#os.system('mplayer ' + d + 'fear.mp3')

def happiness_neutral():

	woody_action.move_to([3,8], [-0.15, -0.15])
	time.sleep(1)
	woody_action.move_to([2,4,9], [26.25, 58.21, -62.02])
	time.sleep(1)
	woody_action.move_to([3,8], [30.06, -27.13])
	time.sleep(1)
	woody_action.move_to([3,8], [58.21, -62.02])
	time.sleep(1)
	woody_action.move_to([3,8], [30.06, -27.13])
	time.sleep(1)
	woody_action.move_to([2,3,8], [-9.53, -0.15, -0.15])
	time.sleep(1)
	woody_action.move_to([3,8], [32.7, -32.11])
	time.sleep(1)
	woody_action.move_to(ids, starting_pose)

	#os.system('mplayer ' + d + 'happiness.mp3')

def sadness():

	woody_action.move_to([2,3], [15.4, 41.5])
	time.sleep(1)
	woody_action.move_to([3], [32.7])
	time.sleep(1)
	woody_action.move_to(ids, starting_pose)
	#os.system('mplayer ' + d + 'sadness.mp3')

#define functions of different behavior
def hello():
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(1.5)

    # nodding
    dxl_io.set_goal_position(dict(zip([2], [16.25])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([2], [-9.53])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([2], [16.25])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([2], [-9.53])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([2], [16.25])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([2], [-9.53])))
    time.sleep(1)


    # waiving hand
    dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(55))))
    dxl_io.set_goal_position(dict(zip([3], [-70])))
    time.sleep(2.5)
    dxl_io.set_moving_speed(dict(zip([5], itertools.repeat(65))))
    dxl_io.set_goal_position(dict(zip([5], [-36.22])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-7.48])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-36.22])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-7.48])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-36.22])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-7.48])))
    time.sleep(0.5)
    dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(30))))
    dxl_io.set_goal_position(dict(zip([3], [32.7])))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip([3], [40])))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(2)



def hugging():
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(2)
    dxl_io.set_goal_position(dict(zip([2], [16.25])))
    time.sleep(2)
    dxl_io.set_goal_position(dict(zip([2], [-9.53])))
    time.sleep(1)


    dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(60))))
    dxl_io.set_goal_position(dict(zip([3, 8], [-10, 10])))
    time.sleep(3)
    dxl_io.set_moving_speed(dict(zip([4,9], itertools.repeat(30))))
    dxl_io.set_goal_position(dict(zip([4, 9], [58.21, -62.02])))
    time.sleep(3)
    dxl_io.set_goal_position(dict(zip([4, 9], [30.06, -27.13])))
    time.sleep(2)
    dxl_io.set_goal_position(dict(zip([4, 9], [58.21, -62.02])))
    time.sleep(3)
    dxl_io.set_goal_position(dict(zip([4, 9], [30.06, -27.13])))
    time.sleep(2)
    dxl_io.set_moving_speed(dict(zip([3,8], itertools.repeat(30))))
    dxl_io.set_goal_position(dict(zip([3,8], [32.7, -32.11])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(2)


def hand_shaking():
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(60))))
   dxl_io.set_goal_position(dict(zip([8], [15.69])))
   time.sleep(2)
   dxl_io.set_moving_speed(dict(zip([10], itertools.repeat(55))))
   dxl_io.set_goal_position(dict(zip([10], [62.32])))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([12], itertools.repeat(60))))
   dxl_io.set_goal_position(dict(zip([12], [0])))
   time.sleep(1)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(30))))
   dxl_io.set_goal_position(dict(zip([8], [5])))
   time.sleep(1)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(60))))
   dxl_io.set_goal_position(dict(zip([8], [15.69])))
   time.sleep(1)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(30))))
   dxl_io.set_goal_position(dict(zip([8], [5])))
   time.sleep(1)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(60))))
   dxl_io.set_goal_position(dict(zip([8], [15.69])))
   time.sleep(1)
   dxl_io.set_goal_position(dict(zip([12], [50])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([10], [8.94])))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(40))))
   dxl_io.set_goal_position(dict(zip([8], [-35])))
   time.sleep(1.5)
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(1.5)

def crying():
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([2, 3, 8], itertools.repeat(55))))
   dxl_io.set_goal_position(dict(zip([2, 3, 8], [13.93, -40, 40])))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([4, 5, 9, 10], itertools.repeat(40))))
   dxl_io.set_goal_position(dict(zip([4,5,9,10], [32.7, 8.65, -29.47, -1.61])))
   time.sleep(0.5)
   dxl_io.set_moving_speed(dict(zip([6,11], itertools.repeat(55))))
   dxl_io.set_goal_position(dict(zip([6,11], [107.48, -111.58])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([6,11], [49.12, -37.39])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([6,11], [107.48, -111.58])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([6,11], [49.12, -37.39])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([6,11], [107.48, -111.58])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([6,11], [49.12, -37.39])))
   time.sleep(0.5)
   dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(30))))
   dxl_io.set_goal_position(dict(zip([3, 8], [22.7, -22.11])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(2)
   
   

def thank_you():
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(1.5)
   dxl_io.set_moving_speed(dict(zip([2, 3, 8], itertools.repeat(55))))
   dxl_io.set_goal_position(dict(zip([3, 8], [-7, 7])))
   time.sleep(1.5)
   dxl_io.set_goal_position(dict(zip([2, 3, 8], [16.25, 23.8, -24.19])))
   time.sleep(1)
   dxl_io.set_goal_position(dict(zip([2], [-9.53])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip([3, 8], [-7, 7])))
   time.sleep(1.5)
   dxl_io.set_goal_position(dict(zip([2, 3, 8], [16.25, 23.8, -24.19])))
   time.sleep(1)
   dxl_io.set_goal_position(dict(zip([2], [-9.53])))
   time.sleep(0.5)
   dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(30))))
   dxl_io.set_goal_position(dict(zip([3, 8], [22.7, -22.11])))
   time.sleep(0.5)
   dxl_io.set_goal_position(dict(zip(ids, start_pose)))
   time.sleep(2)

def dance2():
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(1.5)
    dxl_io.set_moving_speed(dict(zip([1,3,5,8,10], itertools.repeat(65))))
    dxl_io.set_goal_position(dict(zip([3, 8], [1.32, -1.83])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([5, 10], [-64.06, 63.78])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([3, 8], [-86.07, 87.54])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([1, 5, 10], [-81.96, -38.27, 99.85])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([1, 5, 10], [-6.3, -89.88, 43.84])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([1, 5, 10], [-81.96, -38.27, 99.85])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([1, 5, 10], [-6.3, -89.88, 43.84])))
    time.sleep(1)
    dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(30))))
    dxl_io.set_goal_position(dict(zip([3, 8], [32.7, -32.11])))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(2)

def dance3():
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(1.5)
    dxl_io.set_moving_speed(dict(zip([3,5,8,10], itertools.repeat(55))))
    dxl_io.set_goal_position(dict(zip([3, 8], [4, -4])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([5, 10, 7, 12], [-39.15, 45.01, -12.40, 8.05])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([5], [16.25])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-39.15])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([10], [-59.09])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([10], [45.01])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [16.25])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([5], [-39.15])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([10], [-59.09])))
    time.sleep(0.5)
    dxl_io.set_goal_position(dict(zip([10], [45.01])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip([7, 12], [-46.77, 50])))
    dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(30))))
    dxl_io.set_goal_position(dict(zip([3, 8], [32.7, -32.11])))
    time.sleep(1)
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(2)


def main():
	while True:
		idle()

def test():
	anger_disgust()
	time.sleep(5)

	fear_surprise()
	time.sleep(5)

	happiness_neutral()
	time.sleep(5)

	sadness()
	time.sleep(5)

if __name__ == '__main__':
	test()
