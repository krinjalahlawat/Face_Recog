import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance


engine = pyttsx3.init()
engine.say("Welcome students and teachers")
engine.say("Smart face recognition attendance management system")
engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "haarcasecade/haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "TrainingImageLabel/Trainner.yml"
)
trainimage_path = "TrainingImage"
studentdetail_path = (
    "StudentDetails/studentdetails.csv"
)
attendance_path = "Attendance"

window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="white")

# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("1000x500")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="white")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="light blue",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="light blue",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("roman", 20, " bold "),
    ).place(x=220, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True
  
    





a = tk.Label(
    
    window,
    text="Attendance Management System",
    bg="white",
    fg="white",
    bd=10,
    font=("arial", 40),
    
   
)
a.place(x=500,y=700)
a.pack()

img1 = Image.open("UI_Image/topp.png")
img1=img1.resize((1300,180))
rw = ImageTk.PhotoImage(img1)
label = Label(window, image=rw)
label.image = rw
label.place(x=0, y=1)


img = Image.open("UI_Image/iconn1.jpg")
img=img.resize((200,200))
r = ImageTk.PhotoImage(img)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=150, y=240)


ai = Image.open("UI_Image/attend.jpg")
ai=ai.resize((200,230))
a = ImageTk.PhotoImage(ai)

label2 = Label(window, image=a)
label2.image = a
label2.place(x=940, y=240)

vi = Image.open("UI_Image/f6.png")
vi=vi.resize((200,200))
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=550, y=240)





def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="white")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="light blue", relief=RIDGE, bd=2, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="light blue", fg="black", font=("arial", 30),
    )
    titl.place(x=205, y=8)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the Student details",
        bg="white",
        fg="black",
        bd=1,
        font=("arial", 20),
    )
    a.place(x=215, y=70)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="light blue",
        fg="black",
        bd=2,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=2,
        validate="key",
        bg="white",
        fg="light blue",
        relief=RIDGE,
        font=("arial", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="light blue",
        fg="black",
        bd=2,
        relief=RIDGE,
        font=("arial", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=2,
        bg="white",
        fg="light blue",
        relief=RIDGE,
        font=("arial", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="light blue",
        fg="black",
        bd=2,
        relief=RIDGE,
        font=("arial", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=31,
        height=2,
        bd=2,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("arial", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=5,
        font=("arial", 18),
        bg="light blue",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=5,
        font=("arial", 18),
        bg="light blue",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register new student",
    command=TakeImageUI,
    bd=4,
    font=("ananias", 16),
    bg="light blue",
    fg="black",
    height=2,
    width=16,
)
r.place(x=150, y=450)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=4,
    font=("ananias", 17),
    fg="black",
    bg="light blue",
    height=2,
    width=15,
)
r.place(x=550, y=450)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=4,
    font=("ananias", 17),
    bg="light blue",
    fg="black",
    height=2,
    width=15,
)
r.place(x=940, y=450)
r = tk.Button(
    window,
    text="EXIT",
    bd=8,
    command=quit,
    font=("arial", 16),
    bg="light blue",
    fg="black",
    height=1,
    width=4,
)
r.place(x=1160, y=560)

window.mainloop()
