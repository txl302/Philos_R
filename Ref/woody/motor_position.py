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


    print(dxl_io.get_present_position((1,2)))

    



