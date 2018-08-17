import itertools
import numpy
import time

import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()
print('available ports:', ports)  

if not ports:
    raise IOError('No port available.') 

port = ports[0]
print('Using the first on the list', port)

dxl_io = pypot.dynamixel.DxlIO(port)
print('Connected!')

found_ids = dxl_io.scan()
print('Found ids:', found_ids)

if len(found_ids) < 2:
    raise IOError('You should connect at least two motors on the bus for this test.')
#chose all motors and enable torque and set the same speed
ids = found_ids[:]
dxl_io.enable_torque(ids)
speed = dict(zip(ids, itertools.repeat(20)))
dxl_io.set_moving_speed(speed)
dxl_io.set_moving_speed(dict(zip([1,2], itertools.repeat(55))))
dxl_io.set_moving_speed(dict(zip([3,8], itertools.repeat(25))))
    
#set stater pose for each motor
starting_pose=[40.03, -8.65, 41.79, 20.97, -19.5, -47.36, -36.51, -38.86, 72.87, 25.95, 29.47, 46.77]
pose1 = [21.26, 21.26, 43.26, 20.97, -18.91, -47.36, -36.51, -10.41, 69.35, 9.24, 29.47, 47.07]
pose2 = [61.44, 21.26, 9.82, 35.92, -4.55, -47.36, -46.19, -42.96, 67.01, 13.34, 29.47, 46.77]

def init_check():
    dxl_io.set_goal_position(dict(zip(ids, starting_pose)))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, pose1)))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, starting_pose)))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, pose2)))
    time.sleep(1.5)
    dxl_io.set_goal_position(dict(zip(ids, starting_pose)))
    
def move_to(m_id, pose):
    dxl_io.set_goal_position(dict(zip(m_id, pose)))

def main():
    init_check()

if __name__ == '__main__':
    main()
