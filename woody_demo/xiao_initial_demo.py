#this is a test of motors for Philos' arms and neck
#this test goal is to test if motors can work and can let Philos do some gestures
#this test is tested by Leo(Xiao)
import itertools
import numpy
import time
import serial

import pypot.dynamixel

#AMP = 30
#FREQ = 0.5

if __name__ == '__main__':
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
    start_pose=[ -44.13, -5.43, 38.86, 9.24, 35.63, 24.49, 51.47, 50.0, -79.33, 52.64, -112.76, -140.91]
    
    #define functions of different behavior
    def hello():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1.5)
##        dxl_io.set_goal_position(dict(zip([1], [-10])))
##        time.sleep(2)
##        dxl_io.set_goal_position(dict(zip([1], [-80])))
##        time.sleep(2)
        
        # nodding
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)

        # waiving hand
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(55))))
        dxl_io.set_goal_position(dict(zip([3], [-70])))
        time.sleep(3)
        dxl_io.set_moving_speed(dict(zip([5], itertools.repeat(65))))
        dxl_io.set_goal_position(dict(zip([5], [58])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [80])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [58])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [80])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [68])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [80])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([5], [68])))
        time.sleep(0.5)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(30))))
        dxl_io.set_goal_position(dict(zip([3], [-20])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip([3], [20])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(2)
    
        print('Philo says hi')


    def hugging():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(4)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)


        dxl_io.set_moving_speed(dict(zip([3, 8], itertools.repeat(55))))
        dxl_io.set_goal_position(dict(zip([3, 8], [-40,130])))
        time.sleep(3)
        dxl_io.set_moving_speed(dict(zip([4,9], itertools.repeat(30))))
        dxl_io.set_goal_position(dict(zip([4, 9], [50,-49])))
        time.sleep(3)
        dxl_io.set_goal_position(dict(zip([4, 9], [1,-83])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([3,8], itertools.repeat(30))))
        dxl_io.set_goal_position(dict(zip([3,8], [35, 53])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(2)
        print('Philo is hugging hands with you')

    def no_idea():
        dxl_io.set_moving_speed(dict(zip([1], itertools.repeat(55))))
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([1], [-10])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip([1], [-80])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip([1], [-10])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip([1], [-80])))
        time.sleep(1.5)
        dxl_io.set_goal_position(dict(zip([1], [-44])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [-5])))
        print('Philo has no idea')

    def point_close_left():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [15])))
        time.sleep(0.5)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([3], [4])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([6], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([6], [83])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([7], itertools.repeat(65))))
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([6], [8])))
        time.sleep(2)
        
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([3], [15])))
        time.sleep(1)

        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        
    def point_mid_left():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([1], [-15])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([3], [4])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([5], [64])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([6], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([6], [83])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([7], itertools.repeat(65))))
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([6], [8])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([5], [41])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([3], [15])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        
    def point_far_left():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([3], [-10])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([5], [64])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([7], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [30])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([7], [50])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([3], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([3], [15])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)


    def point_close_right():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([2], [15])))
        time.sleep(0.5)
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([8], [83])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([11], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([11], [-150])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([12], itertools.repeat(65))))
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([11], [-97])))
        time.sleep(2)
        
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([8], [50])))
        time.sleep(1)

        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)

    def point_mid_right():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        
        dxl_io.set_goal_position(dict(zip([2], [10])))
        time.sleep(0.5)
        dxl_io.set_goal_position(dict(zip([1], [-75])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([8], [83])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([10], [14.52])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([11], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([11], [-150])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([12], itertools.repeat(65))))
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([11], [-97])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([10], [51])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([8], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)

    def point_far_right():
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([8], [96])))
        time.sleep(2)
        dxl_io.set_goal_position(dict(zip([10], [14.52])))
        time.sleep(2)
        dxl_io.set_moving_speed(dict(zip([12], itertools.repeat(45))))
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-117])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([12], [-141])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip([10], [51])))
        time.sleep(1)
        dxl_io.set_moving_speed(dict(zip([8], itertools.repeat(20))))
        dxl_io.set_goal_position(dict(zip([8], [50])))
        time.sleep(1)
        dxl_io.set_goal_position(dict(zip(ids, start_pose)))
        time.sleep(1)




        

    hello()
    hugging()
    no_idea()
    point_close_left()
    point_close_right()
    point_mid_left()
    point_mid_right()
    point_far_left()
    point_far_right()
    

