import math

def move_to_left(dx, dy, dz):

   L1 = 70;
   L2 = 160;
   L3 = 40;
   L4 = 210;

   theta1 = math.atan(dz/dx)

   if dy>0:
      dxx = dx/math.cos(theta1);
      dyy = dy - L1;
      K1 = (-dxx**2-dyy**2+L2**2+(L3+L4)**2)/(2*L2*(L3+L4));
      theta3 = math.acos(K1)-math.pi/2                                            

      K2 = (L3+L4)*math.sin(math.pi/2-theta3);
      K3 = (L3+L4)*math.sin(theta3)+L2;
      beta = math.atan(K2/K3);
      theta2 = math.atan(dyy/dxx)+beta

   else:
      dxx = dx/math.cos(theta1);
      dyy = -dy + L1;
      K1 = (-dxx**2-dyy**2+L2**2+(L3+L4)**2)/(2*L2*(L3+L4));
      theta3 = math.acos(K1)-math.pi/2                                            

      K2 = (L3+L4)*math.sin(math.pi/2-theta3);
      K3 = (L3+L4)*math.sin(theta3)+L2;
      beta = math.atan(K2/K3);
      theta2 = beta-math.atan(dyy/dxx)

   theta1 = theta1*180/math.pi
   theta2 = theta2*180/math.pi
   theta3 = theta3*180/math.pi

   theta1 = -theta1
   theta2 = -theta2 + 90
   theta3 = theta3 - 90
   

   return [theta1, theta2, theta3]

def main():
   print move_to_left(200.0, 0, -220.0)

if __name__ == '__main__':
   main()
