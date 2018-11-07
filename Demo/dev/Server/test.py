import cv2

cap = cv2.VideoCapture(0)
width = 320
height = 240
#cap.set(3,width);
#cap.set(4,height);
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
print face_cascade

def camera():
    global move1
    global move2
    ret, img = cap.read()
    #print img

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    maxArea = 0  
    x = 0  
    y = 0  
    w = 0  
    h = 0

    for (_x,_y,_w,_h) in faces:
        if _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h
    if maxArea > 0:
        cv2.rectangle(img,(x,y),(x+w,y+h),rectangleColor,4)
        a = x+w/2
        b = y+h/2

        if a>5 and b>5:
            move1 = -85*(a-width/2)/width
            move2 = 14.5*(b-height/2)/height
            #print move1, move2
            return (move1, move2)

def vision():

    while True:
        camera()
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
                        
if __name__ == '__main__':
    vision()