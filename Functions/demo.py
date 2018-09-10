from Emotion import detection
import getpass
import dlib
import cv2
import socket
import threading
import numpy as np
from sklearn.externals import joblib

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(('192.168.1.109', 9901))

s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.bind(('192.168.1.109', 9902))

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s3.bind(('192.168.1.109', 9903))

sr1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sr2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sr3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

emotions = ["anger",  "disgust" ,"fear","happiness", "neutral", "sadness", "surprise"] #Emotion list
user_name = getpass.getuser()
detector = dlib.get_frontal_face_detector() #Face detector
predictor = dlib.shape_predictor("/home/"+user_name+"/Philos_R/Functions/Emotion/shape_predictor_68_face_landmarks.dat")

w1=0.75
w2=1-w1
rtd = detection.real_time_detection()



def reveice_proc(s,sc,sr,addr):
	time_tmp = 0
	while(True):

		data,addr = s.recvfrom(64000)
		data = np.fromstring(data, dtype = 'uint8')
		image = cv2.imdecode(data, 1)
		frame = cv2.resize(image, (320, 240))
		[xlist, ylist] = rtd.get_landmarks(frame,detector,predictor)
		vec_landmark = rtd.get_vectorized_landmark(frame,detector,predictor)*w1
		realtime_data = np.array([])
		if (xlist.size) and (vec_landmark.size):
			Norm_AU_feature = rtd.extract_AU(xlist,ylist)*w2
			vec_AU = np.concatenate((Norm_AU_feature,vec_landmark))
			vec_AU= ((vec_AU-np.min(vec_AU))/np.ptp(vec_AU))
			realtime_data = np.concatenate((realtime_data,vec_AU))
			clf = joblib.load("/home/"+user_name+"/Philos_R/Functions/Emotion/best_landmark_SVM.pkl")
			Y = clf.predict([realtime_data])

			se.sendto(Y, addr)

			if Y == 0:
				print 'anger'
			if Y == 1:
				print 'disgust'
			if Y == 2:
				print 'fear'
			if Y == 3:
				print 'happiness'
			if Y == 4:
				print 'neutral'
			if Y == 5:
				print 'sadness'
			if Y == 6:
				print 'surprise'
		cv2.imshow(sc, image)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def main():

	thread1 = threading.Thread(target = reveice_proc, args = (s1, "robot1", sr1, ("192.168.1.94",9991))
	thread1.start()

	thread2 = threading.Thread(target = reveice_proc, args = (s2, "robot2", sr2, ("192.168.1.45",9991))
	thread2.start()

	thread3 = threading.Thread(target = reveice_proc, args = (s3, "robot3", sr3),("192.168.1.45",9991))
	thread3.start()

if __name__ == '__main__':
	main()
