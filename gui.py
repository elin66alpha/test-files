import tkinter as tk
import facefollow
import facetraining
import faceforpc
import RPi.GPIO as GPIO
import time

def follow():
    label1['text'] = "wait"
    facefollow.follow(1)
def train():
    label1['text'] = "wait"
    facetraining.train(1)
def detect():
    label1['text'] = "wait"
    faceforpc.pc(1)

HEIGHT = 640
WIDTH = 480
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#FFD77D', bd=5)
frame.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')



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