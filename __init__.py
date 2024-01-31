#final touches
import speech_recognition
import pyttsx3
import os
import cv2
import time
from datetime import datetime
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
window=ThemedTk(theme='equilux')
window.configure(themebg='equilux')
window.geometry('500x400+50+25')
window.iconbitmap("Camera (1).ico")
window.title('Camera Project')
window.resizable(False, False)
running=True

r=speech_recognition.Recognizer()
siri=PhotoImage(file='Siri_new_logo.png')



def snd1():
    #os.system("C:\\Users\\anson\\PycharmProjects\\pythonProject1\\Programs\\Github Projects\\CameraProject\\screen_record.mp4")
    koukou=os.path.exists('screen_record.mp4')

    if koukou==True:

        cap = cv2.VideoCapture("screen_record.mp4")

        while (cap.isOpened()):

            ret, frame = cap.read()
            # cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            # cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            rb1.configure(value=0)
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            if ret:
                cv2.imshow("window", frame)
            else:
                print('no video')
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue
            key = cv2.waitKey(1)
            if key % 256 == 27:
                break
                rb1.configure(value=0)


        cap.release()
        cv2.destroyAllWindows()
    else:
        rb1.configure(value=0)

def snd2():
    global running
    running=True
    boubou=os.path.exists('image.png')
    if boubou == True:
        while running:
            image = cv2.imread('image.png')
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("window", image)
            rb2.configure(value=0)
            key = cv2.waitKey(1)
            if key % 256 == 27:
                running=False
                cv2.destroyAllWindows()
                rb2.configure(value=0)

    else:
        rb2.configure(value=0)


def popup():
    PopUp=ThemedTk(theme='equilux')
    PopUp.configure(themebg='equilux')
    PopUp.geometry('200x100+100+100')
    PopUp.iconbitmap("Camera (1).ico")
    PopUp.title('Open File')
    PopUp.resizable(False, False)

    openPhoto=ttk.Button(PopUp,text='Open Photo',command=snd2)
    openPhoto.place(x=50,y=20)

def popupV():
    PopUp=ThemedTk(theme='equilux')
    PopUp.configure(themebg='equilux')
    PopUp.geometry('200x100+100+100')
    PopUp.iconbitmap("Camera (1).ico")
    PopUp.title('Open File')
    PopUp.resizable(False, False)

    openPhoto=ttk.Button(PopUp,text='Play Video',command=snd1)
    openPhoto.place(x=50,y=20)

def takeSelfie():
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    video_capture = cv2.VideoCapture(0)
    count = 0


    while True:

        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break  # terminate the loop if the frame is not read successfully

        # record current time
        now = datetime.now()
        # print(now.time())

        cv2.imshow(
            "My Face Detection Project", video_frame
        )  # display the processed frame in a window named "My Face Detection Project"

        k = cv2.waitKey(1)
        if k % 256 == 27:
            break
        faces = face_classifier.detectMultiScale(
            video_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        if len(faces) > 0 and count <= 1:
            img_name = 'image.png'#"frame_at_time_" + str(now.hour) + "." + str(now.minute) + "." + str(now.second) + ".png"
            cv2.imwrite(img_name, video_frame)  # takes picture
            count += 1
            break

    video_capture.release()
    cv2.destroyAllWindows()
    popup()

def screenRecord():
    speakText('Starting to record')
    cam = cv2.VideoCapture(0)
    recording = True
    speakText('Press escape to end recording')

    output_path = "C:/Users/anson/PycharmProjects/pythonProject1/Programs/Github Projects/CameraProject/screen_record.mp4"
    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (frame_width, frame_height))

    while recording:
        check, frame = cam.read()
        cv2.imshow('video', frame)

        out.write(frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:
            break
    out.release()
    cam.release()  # to release/free up camera before ending so other apps can still use it
    cv2.destroyAllWindows()
    popupV()


    #popup()
def speakText(x):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-400)
    engine.say(x)
    engine.runAndWait()
def voice():
    global running
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=1)
        speakText('Say Something')
        audio2=r.listen(source2)

        try:
            MyText=r.recognize_google(audio2)
        except:
            speakText('Didnt recognise voice, try again')
            commandList.configure(text='Didnt recognise voice, try again')
            voice()
            return
        MyText=MyText.lower()
        speakText('you said'+MyText)
        commandList.configure(text='you said'+MyText)

    if 'quit' in MyText or 'bye' in MyText:
        speakText('Bye, im always here when you need me')
        commandList.configure(text='Bye, im always here when you need me')
        running = False
    elif 'shut down' in MyText:
        speakText('Shutting Down in Five')
        commandList.configure(text='Shutting Down in Five')
        speakText('Four')
        speakText('Three')
        speakText('Two')
        speakText('One')
        os.system('shutdown /s /t 1')
    elif 'restart' in MyText:
        speakText('Restarting in Five')
        commandList.configure(text='Restarting in Five')
        speakText('Four')
        speakText('Three')
        speakText('Two')
        speakText('One')
        os.system('shutdown /r /t 1')
    elif 'log out' in MyText:
        speakText('logging out in Five')
        commandList.configure(text='Logging out in Five')
        speakText('Four')
        speakText('Three')
        speakText('Two')
        speakText('One')
        os.system('shutdown -l')
    elif 'selfie' in MyText or 'picture' in MyText:
        speakText('Sure, smile')
        commandList.configure(text='Sure, smile')
        takeSelfie()
    elif 'record' in MyText or 'video' in MyText or 'film' in MyText:
        screenRecord()
    else:
        speakText('Didnt recognise voice')
        commandList.configure(text='Didnt recognise voice')
        voice()



selfieButton=ttk.Button(window,text='Photo',command=takeSelfie)
selfieButton.place(x=200,y=40)

recordButton=ttk.Button(window,text='Record',command=screenRecord)
recordButton.place(x=200,y=90)

siriButton=ttk.Button(window,image=siri,command=voice)
siriButton.place(x=220,y=200)

commandList=ttk.Label(window,text='Say something: \nShutdown, Restart Log out \nTake Picutre/Video or Quite\n \nNote: Press Esc to exit any window')
commandList.place(x=160,y=260)

cred=ttk.Label(window,text='Programmed by Anson')
cred.place(x=370,y=3)

var = IntVar()
rb1 = ttk.Radiobutton(window, text="Play Video", variable=var, value=1, command=popupV)
rb1.place(x=150,y=130)

var2 = IntVar()
rb2 = ttk.Radiobutton(window, text="View Photo", variable=var2, value=1, command=popup)
rb2.place(x=255,y=130)

window.mainloop()