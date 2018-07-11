import socket; 
import threading; 

import struct; 
import os; 
import time; 
import sys; 
import numpy 
import cv2
import re 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ''

class webCamConnect: 
	def __init__(self, resolution = [640,480], windowName = "Taoge Niubi"): 

		self.resolution = resolution; 
		self.name = windowName; 
		self.mutex = threading.Lock(); 
		self.src=911+15 
		self.interval=0 
		self.path=os.getcwd() 
		self.img_quality = 15 
	def _setSocket(self): 
		self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM); 
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); 
	def connect(self): 
		self._setSocket(); 
		self.socket.connect(self.remoteAddress); 
	def _processImage(self): 
		self.socket.send(struct.pack("lhh",self.src,self.resolution[0],self.resolution[1])); 
		face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
		while(1): 
			info = struct.unpack("lhh",self.socket.recv(12)); 
			bufSize = info[0]; 
			if bufSize: 
				try: 
					self.mutex.acquire(); 
					self.buf=b'' 
					tempBuf=self.buf; 
					while(bufSize):
						tempBuf = self.socket.recv(bufSize); 
						bufSize -= len(tempBuf); 
						self.buf += tempBuf; 
						data = numpy.fromstring(self.buf,dtype='uint8') 
						self.image=cv2.imdecode(data,1) 

						gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)

						faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (150,150))
						
    						for (x,y,w,h) in faces:
							#print x,y,w,h
    							cv2.rectangle(self.image,(x,y),(x+w,y+w),(0,255,0),2)
    							#cv2.circle(self.image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

						cv2.imshow(self.name,self.image) 

				except: 
					print("receive failed") 
					pass; 
				finally: 
					self.mutex.release(); 
					if cv2.waitKey(10) == 27: 
						self.socket.close() 
						cv2.destroyAllWindows() 
						print("abandon connection") 
						break 


	def setWindowName(self, name): 
		self.name = name; 
	def setRemoteAddress(remoteAddress): 
		self.remoteAddress = remoteAddress; 


def func(addr): 
	print("create connection") 
	cam = webCamConnect(); 
	cam.setRemoteAddress(addr)
	cam.connect(); 
	cam._processImage();



def connect():
	
	global s

	data = 'connect' 
	s.sendto(data, ('192.168.1.42', 8014))
	if s.recv(1024) == 'comfirmed':
		s.sendto('test', ('192.168.1.42', 8014))

def disconnect():

	global s

	data = 'disconnect'
	s.sendto(data, ('192.168.1.42', 8014))
	s.close()

def command():
	global table_robot
	global table_function

	while True:
		str = raw_input()

		if str == 'connect':
			connect()

		if str == 'disconnect':
			disconnect()

		if str == 'robot':
			print 'The number of connected robot: %s' %len(table_robot)
			print table_robot

		if str == 'command':
			print 'command'

		if str == 'help':
			print 'Taoge Niubi'

		else:
			print 'enter "help" for more command'

def listen_robot():

	global addr

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('', 8013))

	data, addr = s.recvfrom(1024)

	if data == 'connect':

		print 'Received from %s:%s.' %addr

		s.sendto('comfirmed', addr)

		r_name = s.recv(1024)

		print 'Robot %s online' %r_name

		table_robot.append((r_name, addr))
	

def test():

	global addr

	t_command = threading.Thread(target = command, name = 'command_loop')

	t_func = threading.Thread(target = func, name = 'func_loop', args = (("192.168.1.183", 7999)))

	t_command.start()

	t_func.start()

	t_command.join()

	t_func.join()

if __name__ == '__main__':
	test()