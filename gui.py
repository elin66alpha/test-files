import tkinter as tk
import facefollow
import facetraining
import faceforpc
import RPi.GPIO as GPIO
import time
x0=90
y0=90


def follow():
    label1['text'] = "wait"
    facefollow.follow(1)
def train():
    label1['text'] = "wait"
    facetraining.train(1)
def detect():
    label1['text'] = "wait"
    faceforpc.pc(1)

def servoangle(servo1,servo2,angle1,angle2):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo1, GPIO.OUT)
    GPIO.setup(servo2, GPIO.OUT)
    pwm1 = GPIO.PWM(servo1, 50)
    pwm2 = GPIO.PWM(servo2, 50)
    pwm1.start(8)
    pwm2.start(8)
    dutyCycle1 = angle1 / 18. + 3.
    dutyCycle2 = angle2 / 18. + 3.
    pwm1.ChangeDutyCycle(dutyCycle1)
    pwm2.ChangeDutyCycle(dutyCycle2)
    time.sleep(0.3)
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
servoangle(21,20, x0,y0)
HEIGHT = 500
WIDTH = 1000
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#FFD77D', bd=5)
frame.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')


button1 = tk.Button(frame, text="LEFT", font=40,command=lambda: servoangle(21,20,x0=x0+10,y0))
button1.place(relx=0.3, rely=0.5,relheight=0.2, relwidth=0.2)
button2 = tk.Button(frame, text="HOME", font=40,command=lambda: servoangle(21,20,90,90))
button2.place(relx=0.5, rely=0.5,relheight=0.2, relwidth=0.2)
button3 = tk.Button(frame, text="RIGHT", font=40,command=lambda: servoangle(21,20,x0=x0-10,y0))
button3.place(relx=0.7, rely=0.5,relheight=0.2, relwidth=0.2)
button4 = tk.Button(frame, text="UP", font=40,command=lambda: servoangle(21,20,x0,y0=y0-10))
button4.place(relx=0.5, rely=0.3,relheight=0.2, relwidth=0.2)
button5 = tk.Button(frame, text="DOWN", font=40,command=lambda: servoangle(21,20,x0,y0=y0+10))
button5.place(relx=0.5, rely=0.7,relheight=0.2, relwidth=0.2)


button6 = tk.Button(frame, text="FACE FOLLOW", font=40,command=lambda: follow())
button6.place(relx=0, rely=0,relheight=0.2, relwidth=0.2)
button7 = tk.Button(frame, text="SCAN AND TRAIN", font=40,command=lambda: train())
button7.place(relx=0, rely=0.2,relheight=0.2, relwidth=0.2)
button8 = tk.Button(frame, text="FACE DETECTION", font=40,command=lambda: detect())
button8.place(relx=0, rely=0.4,relheight=0.2, relwidth=0.2)

label1 = tk.Label(frame,bg='#FFD77D', bd=5)
label1.place(relx=0, rely=0.8,relheight=0.2, relwidth=0.2)
label2 = tk.Label(frame,bg='#FFD77D', bd=5)
label2.place(relx=0.8, rely=0.8,relheight=0.2, relwidth=0.2)
label3 = tk.Label(frame,font=70,bg='#FFD77D', bd=5)
label3.place(relx=0.5, rely=0,relheight=0.2, relwidth=0.3)
label3['text'] = "PI DEMO\nESC TO EXIT\nPLS SCAN AND TRAIN FIRST\npi install below\nopencv,opencv-contrib,pillow,numpy"
root.mainloop()