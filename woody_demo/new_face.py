import cv2
import numpy as np
#import serial

#test = serial.Serial('/dev/ttyACM0', 9600)
#test.close()
#test.open()

# This code is based on the 2012 paper "Adaptive Face Recognition for Low-Cost, Embedded Human-Robot Interaction" and Yan Zhang's MS thesis. This represents the face detection algorithm.
# This code is based on keeping track of the mean and standard deviation of the skin pixel values, not just the average color vector
# The algorithm omits the RSC-filter (section 2 of thesis) employed ahead of the AdaBoost classifier to search high-probability areas. I think updating the search region by the placement of the previous face might be good enough.
# NOTE: This algorithm sometimes throws an error if the two cheek regions are not calculated to be the same size. I'm working on how to fix this.
# NOTE: Unlike the algorithm mentioned in the thesis, this uses YUV color space. Here, I track the U-V plane.

# def get_face_coordinates():

x = 0
y = 0
w = 0
h = 0
a = 0
b = 0

cam1 = cv2.VideoCapture(0)
ret_b1 = cam1.set(3, 640)
ret_b1 = cam1.set(4, 480)

ret_b1, imgO = cam1.read()
h1, w1, q1 = imgO.shape #Get the width and height (constants) for the webcam picture. I had to rename the third variable from c1 due to the std dev array.
crop = [0, 0, w1, h1] # xi, yi, xf, yf of cropped picture--defaults to full picture size
frontface = False # We need to set a variable determining whether we can pull color from the cheeks or not. If the face is not front-facing, the color will no longer be valid.

u0 = 150 # Initialize c0.
v0 = 116
C0 = [u0, v0] # Rewrite as list
u1 = 0.25
v1 = 0.25
C1 = [u1, v1] # Initialize standard deviation values
[alpha_x, beta_x, alpha_y, beta_y] = [0, 0, 0, 0] # Initialize these values for half-face calculations
face = () # I have to initialize face up here so that I can call it later.

delta = 50 # Controls how precise we are about picking out face pixels

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# if __name__ == '__main__':
while True:
    face_pixel_ct = 0 # No face pixels found...yet.    
    ret_b1, imgO = cam1.read()
    imgO1 = imgO[crop[1]:crop[3], crop[0]:crop[2]]
    img1 = cv2.cvtColor(imgO, cv2.COLOR_BGR2YUV)
    img2 = img1[crop[1]:crop[3], crop[0]:crop[2]]
    h2, w2, c2 = img2.shape
    face = face_cascade.detectMultiScale(imgO1, 1.3, 5)
    img3 = np.zeros((h1, w1, q1), np.uint8)
    for i in range (1, w2, delta): # Go over all pixels in cropped picture with a step size of delta. We don't scan the entire picture to avoid wasting time.
        for j in range (1, h2, delta):
            l, u, v = img2[j, i, :] # I'm calling the Y value l (for luminance) here to avoid confusion later. I won't be using it.
            #u = np.average(img2[j:j+1, i:i+1, 1]) # Edited to try for smoother face region 
            #v = np.average(img2[j:j+1, i:i+1, 2])
            C = [u,v]
            fU = np.abs(C[0]-C0[0]) # Variation of r, g, b values from the mean
            fV = np.abs(C[1]-C0[1])
            if fU <= C1[0] and fV <= C1[1]: # If the U and V values are within one standard deviation of the mean...or less, as necessary for threshold
                img3[j+crop[1]:j+crop[1]+delta, i+crop[0]:i+crop[0]+delta] = 255
                face_pixel_ct += 1 # Another face pixel found!
    face_binary = img3[crop[1]:crop[3], crop[0]:crop[2]]
    if face != (): # The Haar cascade has already found a face
        frontface= True
        for (x, y, w, h) in face: # Face found in cropped region
            face_binary_pixels = 0 # Number of skin-colored "pixels" (blocks of size delta) in detected face region.
            for i in range (1, w2, delta): # Iterate over all pixel blocks
                for j in range(1, h2, delta):
                    if face_binary[j, i, 1] == 255: # If the pixel is skin-colored
                        face_binary_pixels += 1
                        if i <= (x + w/4):
                            alpha_x += 1 # Pixel is found in the "alpha" region on the x-axis (to the left of the half-face region)
                        elif i >= (x + 3*w/4):
                            beta_x += 1 # Pixel is found in the "beta" region on the x-axis (to the right of the half-face region)
                        if j <= (y + h/4):
                            alpha_y += 1 # Pixel is found in the "alpha" region on the y-axis (to the top of the half-face region)
                        elif j >= (y + 3*h/4):
                            beta_y += 1 # Pixel is found in the "beta" region on the y-axis (to the bottom of the half-face region)
            if face_binary_pixels < 1:
                face_binary_pixels = 1
            alpha_x = float(alpha_x)/face_binary_pixels # Normalizing the values. This will represent the percentage of pixels found in each of these regions.
            beta_x = float(beta_x)/face_binary_pixels
            alpha_y = float(alpha_y)/face_binary_pixels
            beta_y = float(beta_y)/face_binary_pixels
    else:
        frontface = False
        half_face_x1 = 0
        half_face_x2 = 0
        half_face_y1 = 0
        half_face_y2 = 0
        face_pixels = 0
        for i in range (1, w2, delta): # Iterate over all pixel blocks
            for j in range(1, h2, delta):
                if face_binary[j, i, 1] == 255: # If the pixel is skin-colored
                    face_pixels += 1
                    if float(face_pixels)/face_pixel_ct >= alpha_x and half_face_x1 == 0:
                        half_face_x1 = i # Left boundary of half-face region (x)
                    elif float(face_pixels)/face_pixel_ct >= (1 - beta_x) and half_face_x2 == 0:
                        half_face_x2 = i # Right boundary of half-face region (x)
        face_pixels = 0
        for j in range (1, h2, delta): # Iterate over all pixel blocks (I wish I didn't have to do this twice, but I need it once for x and once for y)
            for i in range(1, w2, delta):
                if face_binary[j, i, 1] == 255: # If the pixel is skin-colored
                    face_pixels += 1
                    if float(face_pixels)/face_pixel_ct >= alpha_y and half_face_y1 == 0:
                        half_face_y1 = j # Top boundary of half-face region (y)
                    elif float(face_pixels)/face_pixel_ct >= (1 - beta_y) and half_face_y2 == 0:
                        half_face_y2 = j # Bottom boundary of half-face region (y)
        w = 2 * (half_face_x2 - half_face_x1)
        h = 2 * (half_face_y2 - half_face_y1)
        if w != 0 and h != 0 and w < 2.5*h and h < 2.5*w: # This is my first attempt to prevent false detections, as the program is prone to error. Wide or tall rectangles generally suggest an error.
            face = np.array([[half_face_x1 - w/4, half_face_y1 - h/4, w, h]]) # This makes the list the data type as what is returned from face_cascade.detectMultiScale 
    if face == (): #This is "acting like" we didn't find a face, and resetting to full image
        crop = [0, 0, w1, h1]
    for (x,y,w,h) in face:
        x = x + crop[0] # Transfer coordinates from cropped image to full image
        y = y + crop[1]
        cv2.rectangle(imgO,(x,y),(x+w,y+h),(255,255,0),2)
        crop = [x-w/4, y-h/4, x+5*w/4, y+5*h/4] # Crop window updated. We can change the value of the frame crop as needed.
        cv2.rectangle(img3,(x-w/4,y-h/4),(x+5*w/4,y+5*h/4),(255,255,0),2)
        if frontface == True:
            face_rgn1 = img1[y+h/2:y+2*h/3, x+w/6:x+w/3] # Cheek region 1
            face_rgn2 = img1[y+h/2:y+2*h/3, x+w/2+w/6:x+w/2+w/3] # Cheek region 2
            cv2.rectangle(imgO,(x+w/6,y+h/2),(x+w/3,y+2*h/3),(255,0,255),2) # Rectangles that describe cheek regions
            cv2.rectangle(imgO,(x+2*w/3,y+h/2),(x+5*w/6,y+2*h/3),(255,0,255),2)
            # Taking average u and v values in cheek regions. Yan said that you can resize the picture first to make it smaller and decrease computational time, but with my small webcam I don't need to.
            u0 = np.average([face_rgn1[:, :, 1], face_rgn2[:, :, 1]])
            v0 = np.average([face_rgn1[:, :, 2], face_rgn2[:, :, 2]])
            # Standard deviation values
            u1 = np.std([face_rgn1[:, :, 1], face_rgn2[:, :, 1]])
            v1 = np.std([face_rgn1[:, :, 2], face_rgn2[:, :, 2]])
            C0 = [u0, v0] # Average skin color vector
            C1 = [u1, v1] # Standard deviations
        if crop[0] < 0: # Prevents crop from cutting outside of full image
            crop[0] = 0
        if crop[1] < 0:
            crop[1] = 0
        if crop[2] > w1:
            crop[2] = w1
        if crop[3] > h1: 
            crop[3] = h1
    cv2.imshow('Camera1', imgO)
    # print ('x=',x)
    # cv2.imshow('mask', img3)
    # print ('y=',y)

    if (x > 0):
        a = x + w/2
        b = y + h/2
        print (a, b)
        if (a < 100):
            #test.write('2')
            pass
        elif (a > 220):
            #test.write('1')
            pass
        else:
            #test.write('3')
            pass

    if cv2.waitKey(100) == 27:
        cv2.detroyAllwindows()
        #test.close()
        break
    #cv2.destroyAllwindows()
        # return (a,b)


# while True:
#     [x, y] = get_face_coordinates()
#     print ('coords',(x,y))