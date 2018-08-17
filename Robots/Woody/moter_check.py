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

print dxl_io.get_present_position((1,2,3,4,5,6,7,8,9,10,11,12))
