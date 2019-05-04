from adafruit_servokit import ServoKit
kit = ServoKit(channels = 16)

def move_to(num, pos):
    kit.servo[num].angle = pos

if __name__ == "__main__":
    move_to(1, 120)
    
