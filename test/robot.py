import socket;
import threading; 
import struct; 
import cv2 

import numpy 

class webCamera:
	def __init__(self, resolution = (640, 480), host = ("", 7999)):
		self.resolution = resolution;
		self.host = host;
		self.setSocket(self.host); 
		self.img_quality = 15 


	def setSocket(self, host):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1);
		self.socket.bind(self.host); 
		self.socket.listen(5); 
		print("Server running on port:%d" % host[1]);

	def _processConnection(self, client,addr): 

		camera = cv2.VideoCapture(0) 
		encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),self.img_quality] 

		while(1): 

			(grabbed, self.img) = camera.read() 
			self.img = cv2.resize(self.img,self.resolution) 
			result, imgencode = cv2.imencode('.jpg',self.img,encode_param) 
			img_code = numpy.array(imgencode) 
			self.imgdata = img_code.tostring() 

			client.send(struct.pack("lhh",len(self.imgdata), self.resolution[0],self.resolution[1])+self.imgdata);

			cv2.imshow('object', self.img)

	def run(self): 
		client,addr = self.socket.accept(); 
		self._processConnection(client, addr);


def main(): 
		cam = webCamera(); 
		cam.run(); 
if __name__ == "__main__":
	main();