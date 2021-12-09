from tkinter import *
#Tkinter in python 2
#from GPIOEmulator.EmulatorGUI import GPIO as io
import RPi.GPIO as io
import time

servoPIN = 18
io.setmode(io.BCM)
io.setup(servoPIN,io.OUT)
p = io.PWM(servoPIN, 50)
p.start(2.5)

root = Tk()
#Label(root, text="Angle").grid(row=0)
#e1 = Entry(root)
#e1.grid(row=0, column=1)

has_prev_key_release = None


def on_key_press(event):
    if event.char == "1":
        print(1)
        p.start(2.5)
        p.ChangeDutyCycle(8.75)   #180 degrees
    elif event.char == "2":
        print(2)
        p.start(2.5)
        p.ChangeDutyCycle(2)    #0 degrees
    elif event.char == "4":
        p.stop()
        io.cleanup()
    #w=Label(root1, text="Key Pressed: "+lett)
    #w.place(x=70,y=90)
    
def on_key_release(event):
    global has_prev_key_release
    has_prev_key_release = None
    #time.sleep(2)
    p.ChangeDutyCycle(0)    #0 degrees
    #p.stop()
    #io.cleanup()
    
    print(3)

"""
def cal():
    global dc
    deg1 =e1.get()
    deg = abs(float(deg1))
    dc = 0.056*deg + 2.5
    #p.ChangeDutyCycle(dc)
    print(deg, dc)


b1= Button(root, text = "Enter",bg="pink", command =cal)
b1.grid(row=2, column=1)
b3 = Button(root, text='Quit', bg= "cyan", command=root.quit)
b3.grid(row=2, column=3)
"""

frame = Frame(root, width=100, height=100)
frame.bind("<KeyRelease>", on_key_release)
frame.bind("<KeyPress>", on_key_press)
frame.pack()
frame.focus_set()
root.mainloop()
 
