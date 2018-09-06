from Emotion import detection
import getpass
import dlib
import cv2
import numpy as np
from sklearn.externals import joblib

emotions = ["anger",  "disgust" ,"fear","happiness", "neutral", "sadness", "surprise"] #Emotion list

user_name = getpass.getuser()
#video_capture = cv2.VideoCapture(0) #Webcam object
detector = dlib.get_frontal_face_detector() #Face detector
predictor = dlib.shape_predictor("/home/"+user_name+"/Philos_R/Functions/Emotion/shape_predictor_68_face_landmarks.dat")
#predictor = dlib.shape_predictor("/home/liutao/Philos_R/Functions/Emotion/shape_predictor_68_face_landmarks.dat")
#self.expression=[]


w1=0.75
w2=1-w1
rtd = detection.real_time_detection()
cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    frame = cv2.resize(frame, (320, 240))

    [xlist, ylist] = rtd.get_landmarks(frame,detector,predictor)
    vec_landmark = rtd.get_vectorized_landmark(frame,detector,predictor)*w1
    realtime_data = np.array([])
   
    if (xlist.size) and (vec_landmark.size):
        Norm_AU_feature = rtd.extract_AU(xlist,ylist)*w2
        vec_AU = np.concatenate((Norm_AU_feature,vec_landmark))
        vec_AU= ((vec_AU-np.min(vec_AU))/np.ptp(vec_AU))
        realtime_data = np.concatenate((realtime_data,vec_AU))


        clf = joblib.load("/home/"+user_name+"/Philos_R/Functions/Emotion/landmark_SVM.pkl") 
        Y = clf.predict([realtime_data])


        #self.label.config(fg="red")
            #print 'hi'
        if Y == 0:
            print 'anger'
        if Y ==1:
            print 'disgust'

        if Y == 2:

            print 'fear'
        if Y ==3:
                #v.set("happiness")
                #self.expression.append(3)
            print 'happiness'
        if Y==4:
                #v.set("neutral")
                #self.expression.append(4)
            print 'neutral'
        if Y ==5:
                #v.set("sadness")
                #self.expression.append(5)
            print 'sadness'
        if Y==6:
                #v.set("surprise")
                #self.expression.append(6)
            print 'surprise'

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()