import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

kit.servo[1].angle = 90

##kit.servo[1].angle = 75
##kit.servo[2].angle = 75
##
##kit.servo[3].angle = 80
##kit.servo[4].angle = 80
##
##kit.servo[5].angle = 80
##kit.servo[6].angle = 80
