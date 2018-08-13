L1 = 70; L2 = 160; L3 = 40; L4 = 210;

dx = 336.7767;
dy = -106.7767;
dz = 0;

if dz>0
   theta1 = atan2(-dz,dx)
else
   theta1 = atan2(dz,dx)
end

if dy>0
   dxx = dx/cos(theta1);
   dyy = dy - L1;
   K1 = (dxx^2+dyy^2-L2^2-(L3+L4)^2)/(2*L2*(L3+L4));
   theta3 = acos(K1)                                            

   K2 = (L3+L4)*sin(pi/2-theta3);
   K3 = (L3+L4)*sin(pi/2-theta3)+L2;
   beta = atan2(K2,K3);
   theta2 = atan2(dyy,dxx)+beta
else
   dxx = dx/cos(theta1);
   dyy = -dy + L1;
   K1 = (dxx^2+dyy^2-L2^2-(L3+L4)^2)/(2*L2*(L3+L4));
   theta3 = acos(K1)                                            

   K2 = (L3+L4)*sin(pi/2-theta3);
   K3 = (L3+L4)*sin(pi/2-theta3)+L2;
   beta = atan2(K2,K3);
   theta2 = beta-atan2(dyy,dxx)
end