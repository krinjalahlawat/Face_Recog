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

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = ("C:\\Users\\SSD\\Desktop\\attendancemanagement\\haarcascade_frontalface_default.xml")
trainimagelabel_path = ("C:\\Users\\SSD\\Desktop\\jarvisgui1\\TrainingLabels\\Trainner.yml")
trainimage_path = ("C:\\Users\\SSD\\Desktop\\jarvisgui1\\TrainingImageface")
studentdetail_path = ("C:\\Users\\SSD\\Desktop\\jarvisgui1\\FaceDetails\\facedetails.csv")
#attendance_path = ("C:\\Users\\SSD\\Desktop\\attendancemanagement\\Attendance")

def sample():
    window = Tk()
    window.title("Face recognizer")
    window.geometry("1280x720")
    dialog_title = "QUIT"
    dialog_text = "Are you sure want to close?"
    window.configure(background="black")


    # to destroy screen
    def del_sc1():
        sc1.destroy()


    # error message for name and no
    def err_screen():
        global sc1
        sc1 = tk.Tk()
        sc1.geometry("400x110")
        sc1.iconbitmap("AMS.ico")
        sc1.title("Warning!!")
        sc1.configure(background="black")
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
            font=("times", 20, " bold "),
        ).place(x=110, y=50)


    def testVal(inStr, acttyp):
        if acttyp == "1":  # insert
            if not inStr.isdigit():
                return False
        return True


    
    a = tk.Label(
        window,
        text="ADD SAMPLES FOR FACE RECOGNITION",
        bg="black",
        fg="light blue",
        bd=10,
        font=("arial", 25),
    )
    a.pack()

    ri = Image.open("UI_Image/register.png")
    r = ImageTk.PhotoImage(ri)
    label1 = Label(window, image=r)
    label1.image = r
    label1.place(x=550, y=180)
    #################################################
    def TakeImageUI():
        ImageUI = Tk()
        ImageUI.title("Take sample Image..")
        ImageUI.geometry("780x480")
        ImageUI.configure(background="black")
        ImageUI.resizable(0, 0)
        titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
        titl.pack(fill=X)
        # image and ti
        # heading
        a = tk.Label(
            ImageUI,
            text="Enter the details",
            bg="black",
            fg="light blue",
            bd=10,
            font=("arial", 24),
        )
        a.place(x=280, y=75)

        # ER no
        lbl1 = tk.Label(
            ImageUI,
            text="Enrollment No",
            width=10,
            height=2,
            bg="black",
            fg="light blue",
            bd=5,
            relief=RIDGE,
            font=("times new roman", 12),
        )
        lbl1.place(x=120, y=130)
        txt1 = tk.Entry(
            ImageUI,
            width=17,
            bd=5,
            validate="key",
            bg="black",
            fg="light blue",
            relief=RIDGE,
            font=("times", 25, "bold"),
        )
        txt1.place(x=250, y=130)
        txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

        # name
        lbl2 = tk.Label(
            ImageUI,
            text="Name",
            width=10,
            height=2,
            bg="black",
            fg="light blue",
            bd=5,
            relief=RIDGE,
            font=("times new roman", 12),
        )
        lbl2.place(x=120, y=200)
        txt2 = tk.Entry(
            ImageUI,
            width=17,
            bd=5,
            bg="black",
            fg="light blue",
            relief=RIDGE,
            font=("times", 25, "bold"),
        )
        txt2.place(x=250, y=200)

        lbl3 = tk.Label(
            ImageUI,
            text="Notification",
            width=10,
            height=2,
            bg="black",
            fg="light blue",
            bd=5,
            relief=RIDGE,
            font=("times new roman", 12),
        )
        lbl3.place(x=120, y=270)

        message = tk.Label(
            ImageUI,
            text="",
            width=32,
            height=2,
            bd=5,
            bg="black",
            fg="light blue",
            relief=RIDGE,
            font=("times", 12, "bold"),
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
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="light blue",
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
            bd=10,
            font=("times new roman", 18),
            bg="black",
            fg="light blue",
            height=2,
            width=12,
            relief=RIDGE,
        )
        trainImg.place(x=360, y=350)


    r = tk.Button(
        window,
        text="Register a new sample",
        command=TakeImageUI,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="light blue",
        height=2,
        width=17,
    )
    r.place(x=550, y=480)
    r = tk.Button(
        window,
        text="EXIT",
        bd=10,
        command=quit,
        font=("times new roman", 16),
        bg="black",
        fg="light blue",
        height=2,
        width=17,
    )
    r.place(x=1015, y=560)
    window.mainloop()