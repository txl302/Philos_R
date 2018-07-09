import socket; 
import threading; 
import struct; 
import os; 
import time; 
import sys; 
import numpy 
import cv2
import re 

class webCamConnect: 
	def __init__(self, resolution = [640,480], remoteAddress = ("127.0.0.1", 7999), windowName = "video"): 
		self.remoteAddress = remoteAddress; 
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
	def getData(self, interval): 
		showThread=threading.Thread(target=self._processImage); 
		showThread.start(); 
		if interval != 0:
			saveThread=threading.Thread(target=self._savePicToLocal,args = (interval, )); 
			saveThread.setDaemon(1); 
			saveThread.start(); 
	def setWindowName(self, name): 
		self.name = name; 
	def setRemoteAddress(remoteAddress): 
		self.remoteAddress = remoteAddress; 
	def _savePicToLocal(self, interval): 
		while(1): 
			try: 
				self.mutex.acquire(); 
				path=os.getcwd() + "\\" + "savePic"; 
				if not os.path.exists(path): 
					os.mkdir(path); 
					cv2.imwrite(path + "\\" + time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time())) + ".jpg",self.image) 
			except: 
				pass; 
			finally: 
				self.mutex.release(); 
				time.sleep(interval); 

def main(): 
	print("create connection") 
	cam = webCamConnect(); 

	cam.connect(); 
	cam.getData(cam.interval); 
if __name__ == "__main__": 
	main();
