from Emotion import detection
import getpass
import dlib
import cv2
import socket
import threading
import numpy as np
from sklearn.externals import joblib

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(('192.168.1.71', 9901))

s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.bind(('192.168.1.71', 9902))

s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s3.bind(('192.168.1.71', 9903))

se1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
se2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
se3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

emotions = ["anger",  "disgust" ,"fear","happiness", "neutral", "sadness", "surprise"] #Emotion list
user_name = getpass.getuser()
detector = dlib.get_frontal_face_detector() #Face detector
predictor = dlib.shape_predictor("/home/"+user_name+"/Philos_R/Functions/Emotion/shape_predictor_68_face_landmarks.dat")

w1=0.75
w2=1-w1
rtd = detection.real_time_detection()



def reveice_proc(s,sc,se, port):
	time_tmp = 0
	while(True):
		print (time.time() - time_tmp)
		time_tmp = time.time()

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

			se.sendto(Y, ('192.168.1.45', port))

		cv2.imshow(sc, image)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def ev(n):

	for i in range(n):
		name = "robot" + str(n)
		thread[n] = threading.Thread(target = reveice_proc, args = (s1, name, se1, 999+n))
		thread[n].start()

def main():
	ev(1)

if __name__ == '__main__':
	main()
