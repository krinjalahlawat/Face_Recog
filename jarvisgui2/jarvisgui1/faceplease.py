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
import tkinter.ttk as tkk
import tkinter.font as font
import traceback
import pyttsx3
import sys
flag=""
haarcasecade_path = ("C:\\Users\\SSD\\Desktop\\attendancemanagement\\haarcascade_frontalface_default.xml")
trainimagelabel_path = ("C:\\Users\\SSD\\Desktop\\jarvisgui1\\TrainingLabels\\Trainner.yml")
trainimage_path = "C:\\Users\\SSD\\Desktop\\attendancemanagement\\TrainingImage"
studentdetail_path = ("C:\\Users\\SSD\\Desktop\\jarvisgui1\\FaceDetails\\facedetails.csv")
attendance_path = ("C:/Users/SSD/Desktop/attendancemanagement/Attendance")
# for choose subject and fill attendance
def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()
def fillattendancenew():
    global flag
    def FillAttendance():
        global flag
        sub = tx.get()
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the id !!!"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                    print("yes")
                except:
                    e = "Model not found,please train model"
                    Notifica.configure(
                        text=e,
                        bg="black",
                        fg="yellow",
                        width=33,
                        font=("times", 15, "bold"),
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 70:
                            Subject = tx.get()
                            ts = time.time()
                            print(conf)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im,"recognised face", (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                            flag="recognise"
                        else:
                            Id = "Unknown"
                            #tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im,"unknown face", (x + h, y), font, 1, (0, 25, 255), 4
                            )
                            flag="unrecognise"
                    if time.time() > future:
                        break
                    cv2.imshow("Recognizing face....", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                
                m = "Face recognised succesfully.Granting access "
                Notifica.configure(
                    text=m,
                    bg="black",
                    fg="yellow",
                    width=33,
                    relief=RIDGE,
                    bd=5,
                    font=("times", 15, "bold"),
                )
                text_to_speech(m)

                Notifica.place(x=20, y=250)
                cam.release()
                cv2.destroyAllWindows()
                subject.destroy()
            except Exception:
                traceback.print_exc()
                print("last wale except mein hun")
                #f = "No Face found for attendance"
                #text_to_speech(f)
                cv2.destroyAllWindows()

    ###windo is frame for subject chooser
    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Face recognition")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="Face Recognition",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)
    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )
    sub = tk.Label(
        subject,
        text="Enter id",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Recognise face",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()
    return flag
