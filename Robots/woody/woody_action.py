import itertools
import numpy
import time
import serial

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
start_pose=[ -44.13, -5.43, 38.86, 9.24, 35.63, 24.49, 51.47, 50.0, -79.33, 52.64, -112.76, -140.91]

#define functions of different behavior
def hello():
    dxl_io.set_goal_position(dict(zip(ids, start_pose)))
    time.sleep(1.5)

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

def init():
    print 'visual function initialized'
    init_request = 'connect| visual|' + str_ports
    s.sendto(init_request, ('192.168.1.235', 8014))

def command():
    while True:
        str = raw_input()
        if str == 'connect':
            request = 'connect| visual|' + str_ports
            s.sendto(request, ('192.168.1.235', 8014))
            print 's'
        elif str == 'disconnect':   
            request = 'disconnect| visual|' + str_ports
            s.sendto(request, ('192.168.1.235', 8014))
        elif str == 'help':
            print 'help'
        else:
            print 'enter "help" for more command'

def move_to():
    pass

def main():
    init()
    thread_c = threading.Thread(target = command)
    thread_c.start()

if __name__ == '__main__':
    main()