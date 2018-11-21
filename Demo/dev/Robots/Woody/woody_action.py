import itertools
import numpy
import pypot.dynamixel

import math
import time

from math import *

ports = pypot.dynamixel.get_available_ports()
print('available ports:', ports)  

if not ports:
    raise IOError('No port available.') 

port = ports[0]
print('Using the first on the list', port)

dxl_io = pypot.dynamixel.DxlIO(port)
print('Connected!')

found_ids = dxl_io.scan(range(13))
print('Found ids:', found_ids)

if len(found_ids) < 2:
    raise IOError('You should connect at least two motors on the bus for this test.')
#chose all motors and enable torque and set the same speed
ids = found_ids[:]
dxl_io.enable_torque(ids)
    
def move_to(m_id, speed, pose):
    dxl_io.set_moving_speed(dict(zip(m_id, itertools.repeat(speed))))
    dxl_io.set_goal_position(dict(zip(m_id, pose)))

def get_present_position(m_id):
    p = dxl_io.get_present_position(m_id)
    return p

def Guss(mu, sigma, x):
	f = 1/(sqrt(2*pi)*sigma)*pow(e, (-pow((x - mu), 2)/2))
	return f

def run(m_id, current_pos, des_pos, time_inv):
	current_time = time.time()
	des_time  = current_time + time_inv
	n = len(m_id)
	while True:
		if time.time() <= des_time:
			for i in range(n):
				speed = (des_pos[i] - current_pos[i])*Guss(current_time, 1, time.time())
			move_to(m_id, des_pos, speed)

pos1 = [1.32, -1.83]
pos2 = [-86.07, 87.54]

ids = [3, 8]


if __name__ == '__main__':
	while True:
		run(ids, pos1, pos2, 3)
		time.sleep(3)
		run(ids, pos2, pos1, 3)
		time.sleep(3)
