import itertools
import numpy
import pypot.dynamixel

import math
import time

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

def speed_position():
	speed = 60*math.cos(time.time())
	pose = 60*math.sin(time.time())

	return [speed, pose]

def run():
	result = speed_postion()
	speed = result[0]
	position = result[1]

	move_to(8, speed, postion)

	time.sleep(1)

if __name__ == '__main__':
	run()
