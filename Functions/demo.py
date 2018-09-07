import cv2
import socket
import threading
import numpy
from common import functional

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
	init()
	thread_c = threading.Thread(target = command)
	thread_c.start()
	thread_s1 = threading.Thread(target = play1);
	thread_s1.start();
	thread_s2 = threading.Thread(target = play2);
	thread_s2.start();

	thread_c.join()

def test():
	search_master()



if __name__ == '__main__':
	run()