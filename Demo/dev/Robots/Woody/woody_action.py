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

found_ids = dxl_io.scan(range(13))
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
start_pose=[ -55.28, -9.53, 45.6, 30.06, -7.48, 49.12, -46.77, -44.13, -27.13, 8.94, -37.39, 50.0]
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

    
def move_to(m_id, pose):
    #dxl_io.set_moving_speed(dict(zip(m_id, itertools.repeat(speed))))
    dxl_io.set_goal_position(dict(zip(m_id, pose)))

def get_present_position(m_id):
    p = dxl_io.get_present_position(m_id)
    return p
    

def main():
    #init_check()
    move_to([3,4,5], [-45.0, 54.13358692001617, -27.306476660380607])

if __name__ == '__main__':
    main()
