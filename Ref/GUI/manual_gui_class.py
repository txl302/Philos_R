from Tkinter import*
import time

import sys
import thread

class Manual_GUI():

# BUTTON COMMAND DEFINATION
    def close_window(self):
        self.window.destroy()
        GPIO.cleanup()
        
    
    def reset(self):
       # global LR_bending
       # global FB_bending
        self.LR_bending=7.5
        self.FB_bending=7.5
        self.pwm1.start(self.LR_bending)
        self.pwm2.start(self.FB_bending)
        self.scale_1.set(0)
        self.scale_2.set(0)

    def tip_left(self):  
       # global LR_bending
        self.LR_bending=self.LR_bending+0.25
        if (self.LR_bending>12.5):
            self.LR_bending=12.5
            print 'Reach the Limit.'
        self.pwm2.start(self.LR_bending)


    def tip_right(self):
        #global LR_bending
        self.LR_bending=self.LR_bending-0.25
        if (self.LR_bending<2.5):
            self.LR_bending=2.5
            print 'Reach the Limit.'
        self.pwm2.start(self.LR_bending)


    def tip_up(self):
        #global FB_bending
        self.FB_bending=self.FB_bending+0.25
        if (self.FB_bending>12.5):
            self.FB_bending=12.5
            print 'Reach the Limit.'
        self.pwm1.start(self.FB_bending)

    
    def tip_down(self):
        #global FB_bending
        self.FB_bending=self.FB_bending-0.25
        if (self.FB_bending<2.5):
            self.FB_bending=2.5
            print 'Reach the Limit.'
        self.pwm1.start(self.FB_bending)



    def LR_bend(self,LR_angle):
    
        LR_angle=float (LR_angle)
    
        if (LR_angle>=0):
            LRdutycycle = 7.5-10.0/180.0*LR_angle
        else:
            LRdutycycle = 7.5+10.0/180.0*abs(LR_angle)
        LRdutycycle= round(LRdutycycle,2)
        global LR_bending
        LR_bending= LRdutycycle
        self.pwm2.start(LRdutycycle)
  
    def FB_bend(self,FB_angle):
    
        FB_angle=float (FB_angle)
        if (FB_angle>=0):
            FBdutycycle = 10.0/180.0*FB_angle+7.5
        else:
            FBdutycycle = 7.5-10.0/180.0*abs(FB_angle)
        FBdutycycle= round(FBdutycycle,2)
        global FB_bending
        FB_bending= FBdutycycle
        self.pwm1.start(FBdutycycle)


    def motor_up(self):
        self.WaitTimedef()
       # global switch
        self.switch=1
        GPIO.output(self.DIR,self.Up)
        thread.start_new_thread(self.stepmotor, ())
    
    def motor_down(self):
        self.WaitTimedef()
        #global switch
        self.switch=1
        GPIO.output(self.DIR,self.Down)#Up=1;Down=0
        thread.start_new_thread(self.stepmotor, ())

    def WaitTimedef(self):
        #global WaitTime

        if (self.v.get()==1):
            self.WaitTime=0.001
        elif (self.v.get()==2):
            self.WaitTime=0.0008
        else:
            self.WaitTime=0.0006
    
    def motor_stop(self):
        self.WaitTimedef()
        #global switch
        self.switch=0
    # thread.exit_thread()


    def stepmotor(self):
        #global switch
        #global WaitTime
        while (self.switch == 1):
            GPIO.output(self.STEP,1)
            time.sleep(self.WaitTime)
            GPIO.output(self.STEP,0)
            time.sleep(self.WaitTime)

    def __init__(self):
# GPIO MODE SETTING
        servo1=11
        servo2=13
        self.STEP=15
        self.DIR=16
        self.Up=1
        self.Down=0
        self.WaitTime=0.0006

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.STEP,GPIO.OUT)
        GPIO.output(self.STEP,0)
        GPIO.setup(self.DIR,GPIO.OUT)

        GPIO.setup(servo1,GPIO.OUT)
        GPIO.setup(servo2,GPIO.OUT)


# STEPPER MOTOR Global Variables
        self.LR_bending=7.5
        self.FB_bending=7.5
        self.switch=0 

# PWM FREQENCY SETTING
        self.pwm1=GPIO.PWM(servo1,50)
        self.pwm2=GPIO.PWM(servo2,50)
    
# CREATE A INTERFACE 
        self.window = Tk()
        self.window.geometry('400x320')
        self.window.title('IntuBot Interface')
        self.v= IntVar()

# TITLE 
        label_1=Label (self.window,text='IntuBot Manual Control Interface', bg= 'black', fg='white', font= 'non 15 bold')
        label_1.pack(fill=X)


# EXIT BUTTON (TO BE IN THE MIDDLE AT THE BOTTOM, THE LINES HAVE TO BE HERE)
        button_10=Button(self.window, text='Exit',width=14,command=self.close_window)
        button_10.pack(side= BOTTOM,pady=(0,5))

# TWO LABEL FRAMES FOR BENDING MOTION AND LINEAR MOTION
        frame_1= LabelFrame(self.window,text='Bending Motion',width=250,heigh=310,bd=1)
        frame_1.pack(side=LEFT,anchor=W,padx=(10,5))
        frame_2= LabelFrame(self.window, text='Linear Motion',width=130,heigh=310,bd=1)
        frame_2.pack(side=LEFT,padx=(5,10))

# RESET BUTTON FOR STYLET TIP BENDING 
        button_1=Button(frame_1, text='Reset',width=7,command=self.reset)
        button_1.pack()
        

#label_1=Label (frame_1,fg='gray', font= 'non 9')
#label_1.pack(side=BOTTOM,pady=(0,5))
#label_print(label_1)

# TWO SLIDERS FOR TIP LEFR/RIGHT AND UP/DOWN COARSE TUNING
        self.scale_2=Scale(frame_1,orient=VERTICAL,length=150,from_=90,to=-90,tickinterval=45,resolution=15,command=self.FB_bend)
        self.scale_2.pack(side=RIGHT)
        self.scale_1=Scale(frame_1,orient=HORIZONTAL,length=150,from_=-90,to=90,tickinterval=45,resolution=15,command=self.LR_bend)
        self.scale_1.pack(padx=10)

# FOUR BOTTONS FOR TIP FINING TUNING
        button_2=Button(frame_1, text='Up',width=3,command=self.tip_up)
        button_2.pack(pady=10,padx=10)


        button_3=Button(frame_1, text='Down',width=3,command=self.tip_down)
        button_3.pack(side=BOTTOM,pady=10,padx=10)
        button_4=Button(frame_1, text='Left',width=3,command=self.tip_left)
        button_4.pack(side=LEFT,pady=10,padx=10)
        button_5=Button(frame_1, text='Right',width=3,command=self.tip_right)
        button_5.pack(side=RIGHT,pady=10,padx=10)

# TWO BUTTONS FOR STEPPER MOTOR UP AND DOWN
        button_8=Button(frame_2, text='Up',width=7)
        button_8.pack(padx=10,pady=25)
        button_8.bind('<ButtonPress-1>', lambda event: self.motor_up())
        button_8.bind('<ButtonRelease-1>', lambda event:  self.motor_stop())
        button_9=Button(frame_2, text='Down',width=7)
        button_9.pack(padx=10,pady=25)
        button_9.bind('<ButtonPress-1>', lambda event: self.motor_down())
        button_9.bind('<ButtonRelease-1>', lambda event: self.motor_stop())

# THREE RADIO BUTTONS FOR DIFFERENT STEP SETTINGS
        R1= Radiobutton(frame_2,text='Low speed',value=1,variable=self.v)
        R1.pack(anchor=W)
        R2= Radiobutton(frame_2,text='Medium speed',value=2,variable=self.v)
        R2.pack(anchor=W)
        R3= Radiobutton(frame_2,text='High speed',value=3,variable=self.v)
        R3.pack(anchor=W,pady=(0,10))
        R3.invoke() # default choice


# DISPLAY ALL THE SETTINGS
        self.window=mainloop()
        
# GPIO CLEAN
        GPIO.cleanup()
