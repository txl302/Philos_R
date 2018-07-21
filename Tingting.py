import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sum1_i = 0
sum1_j = 0
count1 = 0

temp = 0

event = 1
temp_now = 0
temp = 0

mail_host = 'smtp.gmail.com'
mail_user = 'xueting19910330'
mail_pass = '123456789team28'
mail_postfix = 'gmail.com'

mailto_list = ['xueting19910330@gmail.com']

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')		

cam1 = cv2.VideoCapture(1)
#cam2 = cv2.VideoCapture(2)
#cam3 = cv2.VideoCapture(3)
#cam4 = cv2.VideoCapture(0)

ret_b1 = cam1.set(3,320)
ret_b1 = cam1.set(4,240)

ret_b1, bg1 = cam1.read()
#ret_b2, bg2 = cam2.read()
#ret_b3, bg3 = cam3.read()
#ret_b4, bg4 = cam4.read()

bg_b1 = cv2.cvtColor(bg1, cv2.COLOR_BGR2GRAY)
#bg_b1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#bg_b1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#bg_b1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('bg_b1', bg_b1)


def motion_detection():
	return 0 
	


def people_detecton():
	return 0

def send_mail(to_list, sub, content):
	me = mail_user + "@" + mail_postfix
	msg = MIMEText(content, _subtype='plain', _charset='gb2312')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		server = smtplib.SMTP()
		server.connect(mail_host, 587)
		
		server.ehlo()
		server.starttls()

		server.login(mail_user, mail_pass)
		server.sendmail(me ,to_list, msg.as_string())
		server.close()
		return True
	except Exception, e:
		print str(e)
		return False


while True:

	if(event >= 3):
		print 'ready to send email'
		if send_mail(mailto_list, "Tingting is beautiful", "Tingting is smart"):
			print "email sent"
		else:
			print "email sending failed"


		face = face_cascade.detectMultiScale(img1, 1.2, 5)
            	for (x,y,w,h),n in face:                
                	cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,255),2)
                	print 'people detected'
		
		#print 'email has been sent'

	elif (event < 3):

		ret1 = cam1.set(3,320)
		ret1 = cam1.set(4,240)
		#ret2 = cam1.set(3,320)
		#ret2 = cam1.set(4,240)
		#ret3 = cam1.set(3,320)
		#ret3 = cam1.set(4,240)
		#ret4 = cam1.set(3,320)
		#ret4 = cam1.set(4,240)

		ret1, img1 = cam1.read()
		#ret2, img2 = cam2.read()
		#ret3, img3 = cam3.read()
		#ret4, img4 = cam4.read()


		gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


		cv2.imshow('Tingting1', gray1)
		#cv2.imshow('Tingting2', img2)
		#cv2.imshow('Tingting3', img3)
		#cv2.imshow('Tingting4', img4)

		det1 = np.zeros(bg_b1.shape, np.uint8)


		det1 = cv2.absdiff(gray1, bg_b1)

		#s = det1.item((50, 50))
		#print s

		for i in range (1,319,20):
			for j in range (1,219,20):
				if (det1.item(j,i)>10):
					sum1_i = sum1_i + i
					sum1_j = sum1_j + j
					count1 = count1 + 1
		if(count1 > 30):
			print "object detected from camera1"
			

			face = face_cascade.detectMultiScale(img1, 1.3, 5)
            		for (x,y,w,h) in face:                
                		cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,255),2)
                		print 'people detected'

			cv2.imshow('high_res1', img1)

			temp_now = count1
			count1 = 0

			event = 2



	elif(event == 2):

		face = face_cascade.detectMultiScale(img1, 1.3, 5)
            	for (x,y,w,h) in face:                
                	cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,255),2)
                	print 'people detected'

		cv2.imshow('high_res1', img1)
		upper = temp
		lower = temp - 20
		if (temp_now > upper):
			print 'The object is approching from the camera1 side'
			print 'alert'
			event = 3
			
		elif(count1 <= upper and count1 >= lower):
			event = 2
		else:
			event = 1

	temp = temp_now

	print event,temp_now, temp





	cv2.imshow('object', det1)


	

	count1 = 0
	if cv2.waitKey(100) == 27:
		break
cv2.destroyAllwindows()
