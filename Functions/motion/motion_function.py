import math

import socket
import threading
import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ports = []

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

lo_addr = get_host_ip()

av_ports = [9998, 9999]

for i in range(len(av_ports)):
   ports.append((lo_addr, av_ports[i]))


s1.bind(ports[0])
s2.bind(ports[1])
str_ports = str(ports)

def init():
   print 'motion function initialized'
   init_request = 'connect| motion|' + str_ports
   s.sendto(init_request, ('192.168.1.235', 8014))

def command():
   while True:
      str = raw_input()
      if str == 'connect':
         request = 'connect| motion|' + str_ports
         s.sendto(request, ('192.168.1.235', 8014))
      elif str == 'disconnect':  
         request = 'disconnect| motion|' + str_ports
         s.sendto(request, ('192.168.1.235', 8014))
      elif str == 'help':
         print 'there is no help'
      else:
         print 'enter "help" for more command'

def move_to_left(dx, dy, dz):

   L1 = 70;
   L2 = 160;
   L3 = 40;
   L4 = 210;

   if dz>0:
      theta1 = math.atan(-dz/dx)
   else:
      theta1 = math.atan(dz/dx)

   if dy>0:
      dxx = dx/math.cos(theta1);
      dyy = dy - L1;
      K1 = (dxx**2+dyy**2-L2**2-(L3+L4)**2)/(2*L2*(L3+L4));
      theta3 = amath.cos(K1)                                            

      K2 = (L3+L4)*math.sin(math.pi/2-theta3);
      K3 = (L3+L4)*math.sin(math.pi/2-theta3)+L2;
      beta = math.atan(K2,K3);
      theta2 = math.atan(dyy,dxx)+beta
   else:
      dxx = dx/math.cos(theta1);
      dyy = -dy + L1;
      K1 = (dxx**2+dyy**2-L2**2-(L3+L4)**2)/(2*L2*(L3+L4));
      theta3 = math.acos(K1)                                            

      K2 = (L3+L4)*math.sin(math.pi/2-theta3);
      K3 = (L3+L4)*math.sin(math.pi/2-theta3)+L2;
      beta = math.atan(K2/K3);
      theta2 = beta-math.atan(dyy/dxx)

   print theta1,theta2,theta3

def move_to_right(dx, dy, dz):
   pass

def move():
   move_to_left(dx, dy, dz)

def run():
   thread_c = threading.Thread(target = command)
   thread_c.start()

def main():
   init()
   run()

if __name__ == '__main__':
   main()