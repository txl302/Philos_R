import numpy as np
import cv2
import screeninfo
import random
import time


def expression_rob(sel):
    screen_id = 0
    is_color = False
 
    # get the size of the screen
    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height

    if(sel == 1):
        image = cv2.imread('expression/normal.png')
    elif(sel == 2):
        image = cv2.imread('expression/angry.png')
    elif(sel == 3):
        image = cv2.imread('expression/sad.png')
    elif(sel == 4):
        image = cv2.imread('expression/superise.png')

 
    window_name = 'projector'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, image)



 
if __name__ == '__main__':
    while True:

        expression_rob(random.randint(1,4))   
        time.sleep(20)


    cv2.waitKey()
    cv2.destroyAllWindows()
