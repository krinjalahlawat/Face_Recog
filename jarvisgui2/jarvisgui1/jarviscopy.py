import sys
import PyQt5
import pyttsx3
import datetime
from requests.api import request
import speech_recognition as sr
import smtplib
from secrets import senderemail,epwd
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import PyPDF2
import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import clipboard
import json
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from jarvisgui import Ui_MainWindow
import screen_brightness_control as sbc
import IP2Location
import os
import ipinfo
import pyjokes
import psutil
engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def date():
    year=int(datetime.datetime.now().year)
    mo=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak(day)
    speak(mo)
    speak(year)
def wishme():
    speak("hello sir")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    elif hour>=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")
    speak("jarvis at your service sir Please tell how may i help you")
def takecommand(self):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        self.query=r.recognize_google(audio,language="en-in")
        print(self.query)
    except Exception as e:
        print(e)
        speak("say that again")
        return 'None'
    return self.query
def sendemail(receiver,subject,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    email=EmailMessage()
    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    speak("mail sent succesfully")
def sendwhatsappmsg(phone_no,message):
    Message=message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
    speak("message has been sent sir")
    
def pdf_reader(pdf):
    book=open(pdf,'rb')
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    speak(f"total number of pages in this book is {pages}")
    speak("sir please tell the page number from which you want to read")
    pg=int(takecommand())
    page=pdfreader.getPage(pg)
    text=page.extractText()
    print(text)
    speak(text)
def news(tp):
    newsapi=NewsApiClient(api_key='73ca6eda9f7a4b5c8f9ac8753abe7ddc')
    data=newsapi.get_top_headlines(q=tp,language='en',page_size=5)
    newsdata=data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    speak("thats all for now sir, i will update you in some time")
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        #self.taskexecution()
        speak("please say wakeup to continue")
        while True:
            self.query=self.takecommand()
            if "wake up" in self.query:
                self.taskexecution()
            elif "good bye" in self.query:
                speak("ok bye sir i am going have a good day and dont forget to call me whenever you need")
                sys.exit()
    
    def taskexecution(self):
        wishme()
        while True:
            self.query=self.takecommand().lower()
            if "email" in self.query:
                email_list={'me':'piyushmadan52@gmail.com',
                            'chachu':'anil.inbox03@gmail.com',
                            'arya':'priyanshu.arya18@outlook.com',
                            'now':'srivastavajigeesha74@gmail.com',
                            'mayank':'mmittal123456@gmail.com',
                            'jyoti':'jyotigohri8@gmail.com'
                            }
                try:
                    try:
                        speak("to whom shall i send this mail sir")
                        name=takecommand(self).lower()
                        receiver=email_list[name]
                        speak("what is the subject of the mail sir")
                        subject=takecommand(self)
                        speak("what shall i say sir")
                        content=takecommand(self)
                        sendemail(receiver,subject,content)
                        sleep(1)
                        speak("anything else for which i may assist you sir")
                    except Exception as e:
                        print(e)
                        speak("error")
                        speak("sorry sir please tell me again i was unable to listen")
                except Exception as e:
                    print(e)
                    speak("unable to send mail")
            elif "tell date" in self.query:
                date()
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "time" in self.query:
                time()
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "describe" in self.query:
                speak("hello sir this is jarvis your personal assistant i can handle all your tasks sir like i will keep you update about time and date send your emails and whatsapp messages can tell you about the latest news and can solve your calculations will help you search anything on google wikipedia youtube can open any of your apps can read your books and pdf can update you about the weather and can tell you your location i can also access your phone to some extent can make calls and send text messages and also can take control your keyboard like volume and brightnss take screenshots if you are unhappy with someone i can lift your mood by telling you some jokes and finally can manage your data and show you your task manager at last shutdown your laptop ")
                speak("so these are the tasks")
                speak("what are the tasks that you want me to perform")
            elif 'message' in self.query:
                user_name={
                    'bua': 
                    '+91 9105826408',
                    'mother':
                    '+91 7895625156',
                    'father':
                    '+91 9149354065',
                    'mama':
                    '+91 9760096888',
                    'sunaina chachi':
                    '+91 9876208047',
                    'jyoti':
                    '+91 9897896688',
                    'arya':
                    '+91 7310619574',
                    'mayank':
                    '+91 6397305243',
                    'vinny chachu':
                    '+91 9816644758',
                    'chachu':
                    '+91 9810990233',
                    'now':
                    '+91 7906259560'

                }
                try:
                    try:
                        speak("to whom shall i send this message sir")
                        name=takecommand(self)
                        name=name.lower()
                        phone_no=user_name[name]
                        speak("what is the message sir")
                        message=takecommand(self)
                        sendwhatsappmsg(phone_no,message)
                        sleep(1)
                        speak("anything else for which i may assist you sir")
                    except Exception as e:
                        print(e)
                        speak("error")
                        speak("sorry sir please tell me again i was unable to listen")
                except Exception as e:
                    print(e)
                    speak("unable to send message")

            elif 'wikipedia' in self.query:
                    speak("searching on wikipedia")
                    self.query=self.query.replace('wikipedia','')
                    result=wikipedia.summary(self.query,sentences=2)
                    print(result)
                    speak(result)
                    sleep(1)
                    speak("anything else for which i may assist you sir")
            elif "google" in self.query:
                try:
                    speak("what you want to search sir")
                    search=takecommand(self)
                    wb.open('https://www.bing.com/search?q='+search)
                    speak("the tab has been opened sir")
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif "youtube" in self.query:
                try:
                    speak("what should i search on youtube sir")
                    topic=takecommand(self)
                    pywhatkit.playonyt(topic)
                    speak("results are ready sir opening youtube")
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif "shutdown" in self.query:
                pywhatkit.shutdown(time=90)
                speak("powering off in 90 seconds")
            
            elif "cancel" in self.query:
                pywhatkit.cancelShutdown()
                speak("shutdown cancelled")
                sleep(1)
                speak("anything else for which i may assist you sir")
            
            elif "read a book" in self.query:
                try:
                    bookname={"friends":"C:/courage/5_6228497839639495141.pdf"
                    }
                    speak("please say the book you want to read")
                    name=takecommand(self)
                    pdf=str(bookname[name])
                    book=open(pdf,'rb')
                    pdfreader=PyPDF2.PdfFileReader(book)
                    pages=pdfreader.numPages
                    speak(f"total number of pages in this book is {pages}")
                    speak("sir please tell the page number from which you want to read")
                    pg=int(takecommand(self))
                    page=pdfreader.getPage(pg)
                    text=page.extractText()
                    print(text)
                    speak(text)
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            
            elif "weather" in self.query:
                try:
                    speak("for which city sir do you want to get the current weather")
                    search=takecommand(self)
                    api_key="7e0c1b211b98012daf3d4a030f015820"
                    base_url="http://api.openweathermap.org/data/2.5/weather?"
                    city_name=search
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response=requests.get(complete_url)
                    x=response.json()
                    if x["cod"]!="404":
                        y=x["main"]
                        ct=y["temp"]
                        c=round((ct-273.15))
                        hu=y["humidity"]
                        z=x["weather"]
                        desc=z[0]["description"]
                        speak(f"in {city_name},the temperature is {c} humidity is {hu} and current weather is {desc}")
                        sleep(1)
                        speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            
            elif 'news' in self.query:
                try:
                    speak("for which topic sir you want to listen the news")
                    t=takecommand(self)
                    tp=str(t)
                    news(tp)
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif "location" in self.query:
                try:
                    speak("wait sir let me check")
                    try:
                        ipadd=requests.get("https://api.ipify.org").text
                        print(ipadd)
                        access_token='a6943c218735e9'
                        handler=ipinfo.getHandler(access_token)
                        details=handler.getDetails(ipadd)
                        city=details.city
                        country=details.country_name
                        speak(f"sir i am not sure , but i think we are in {city} city of country {country} ")
                        sleep(1)
                        speak("anything else for which I may assist you sir")
                    except Exception as e:
                            speak("sorry sir due to network issue i am not able to find where we are")
                            pass     
                except:
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif 'convert text to speech' in self.query:
                text=clipboard.paste()
                speak(text)
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "screenshot" in self.query:
                try:
                    speak("sir please tell me the name for this screenshot file")
                    name=takecommand(self).lower()
                    speak("please sir hold the screen i am taking the screenshot")
                    sleep(3)
                    img=pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("screenshot taken and saved it to our main folder")
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif "volume up" in self.query:
                pyautogui.press("volumeup")
                speak("volume upped sir")
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "volume down" in self.query:
                pyautogui.press("volumedown")
                speak("volume lowered sir")
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "mute" in self.query:
                pyautogui.press("volumemute")
                speak("volume muted sir")
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "unmute" in self.query:
                pyautogui.press("volumemute")
                sleep(1)
                speak("volume unmuted sir")
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "brightness" in self.query:
                try:
                    current=sbc.get_brightness()
                    speak(f"current brightness is {current} sir to which value should i set the brightness ")
                    bright=int(takecommand(self))
                    set=sbc.set_brightness(bright)
                    speak(f"brightness set to {set} percent")
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell me again i was unable to listen")
            elif "copy text" in self.query:
                try:
                    speak("please speak the text that you want to copy on clipboard sir")
                    text=str(takecommand(self))
                    clipboard.copy(text)
                    speak("text copied sir")
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("error")
                    speak("sorry sir please tell again i was unable to listen")
            elif "joke" in self.query:
                speak(pyjokes.get_joke("en","all"))
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "internet speed" in self.query:
                import pyspeedtest
                s=pyspeedtest.SpeedTest(host="c.speedtest.net")
                d=s.download()
                ping=s.ping()
                speak(f"sir we have {d} bits per second as our downloading speed ping is {ping}")
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "cpu" in self.query or "battery" in self.query:
                usage=str(psutil.cpu_percent())
                speak("CPU is at"+usage)
                battery=psutil.sensors_battery()
                speak("Battery is at")
                speak(battery.percent)
                sleep(1)
                speak("anything else for which i may assist you sir")
            elif "open apps" in self.query:
                apps={"vs code":'C:\\Users\\piyush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
                      "etoos india":'C:\\Program Files (x86)\\EtoosIndia\\EtoosIndia.exe',
                      "telegram":'C:\\Users\\piyush\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe',
                      "browser":'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
                      "zoom":'C:\\Users\\piyush\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe',
                      "notepad":'C:\\Windows\\system32\\notepad.exe'
                      }
                try:
                        speak("please tell the name of the app you want to open")
                        name=takecommand(self).lower()
                        location=apps[name]
                        os.startfile(location)
                        speak(f"opening {name} sir")
                        sleep(1)
                        speak("anything else for which i may assist you sir")

                except Exception as e:
                        print(e)
                        speak("error")
                        speak("sorry sir please tell again i was unable to listen")
            elif "task" in self.query:
                try:
                    speak("what should i note down sir")
                    data=str(takecommand(self))
                    speak("you said me to remember"+data+"sir")
                    remember=open('data.txt','w')
                    remember.write(data)
                    remember.close()
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("sorry sir please tell again i was unable to listen ")
            elif "do you remember" in self.query:
                try:
                    remember=open('data.txt','r')
                    speak("you told me to remember"+remember.read())
                    remember.close()
                    sleep(1)
                    speak("anything else for which i may assist you sir")
                except Exception as e:
                    print(e)
                    speak("sorry sir please tell again i was unable to listen")
            elif "offline" in self.query:
                speak("I am going offline sir You can call me anytime sir")
                break

    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1
            audio=r.listen(source)
        try:
            print("Recognizing..")
            self.query=r.recognize_google(audio,language="en-in")
            print(self.query)
        except Exception as e:
            print(e)
            speak("say that again")
            return 'None'
        return self.query
startExecution=MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:/Users/SSD/Desktop/jarvisgui1/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:/Users/SSD/Desktop/jarvisgui1/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:/Users/SSD/Desktop/jarvisgui1/Ironman_zps08caec09.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()
    def showtime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())
