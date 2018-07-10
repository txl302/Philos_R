import socket;
import threading; 
import struct; 
import cv2 
import time 
import os 
import numpy 

class webCamera:
	def __init__(self, resolution = (640, 480), host = ("", 7999)):
		self.resolution = resolution;
		self.host = host;
		self.setSocket(self.host); 
		self.img_quality = 15 
	def setImageResolution(self, resolution):
		self.resolution = resolution;
	def setHost(self, host):
		self.host = host;
	def setSocket(self, host):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1);
		self.socket.bind(self.host); 
		self.socket.listen(5); 
		print("Server running on port:%d" % host[1]);
	def recv_config(self,client):
		info = struct.unpack("lhh",client.recv(12));
		if info[0]>911:
			self.img_quality=int(info[0])-911
			self.resolution=list(self.resolution) 
			self.resolution[0]=info[1] 
			self.resolution[1]=info[2] 
			self.resolution=tuple(self.resolution) 
			return 1 
		else :
			return 0 
	def _processConnection(self, client,addr): 
		if(self.recv_config(client)==0): 
			return
		camera = cv2.VideoCapture(0) 
		encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),self.img_quality] 

		while(1): 
			time.sleep(0.13) 
			(grabbed, self.img) = camera.read() 
			self.img = cv2.resize(self.img,self.resolution) 
			result, imgencode = cv2.imencode('.jpg',self.img,encode_param) 
			img_code = numpy.array(imgencode) 
			self.imgdata = img_code.tostring() 
			try: 
				client.send(struct.pack("lhh",len(self.imgdata), self.resolution[0],self.resolution[1])+self.imgdata);
			except: 

				camera.release() 
				f.close() 
				return; 
	def run(self): 
		client,addr = self.socket.accept(); 
		self._processConnection(client, addr);


def main(): 
		cam = webCamera(); 
		cam.run(); 
if __name__ == "__main__":
	main();