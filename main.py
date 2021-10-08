import speech_recognition as sr
import pyttsx3
from tkinter import *

root = Tk()
root.title('Speech to text')
root.configure(bg='yellow')
root.geometry('500x90+200+50')
root.resizable(False, False)
root.iconbitmap('speech.ico')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def recognize():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        audio = r.listen(source)
        text = r.recognize_google(audio)
        text = '{}'.format(text)
        varname.set(text)

def clear():
    varname.set('')

label1 = Label(root, text='SPEECH TO TEXT', bg='yellow', fg='black', font=('times',15,'italic bold'))
label1.place(x=130,y=5)

label2 = Label(root, text='Your text: ', bg='yellow', fg='black', font=('times',15,'italic bold'))
label2.place(x=10,y=50)

varname = StringVar()
entry1 = Entry(root, textvariable=varname, bg='white', width=30,font=('times',15,'italic bold'))
entry1.place(x=110, y=52)

speak = Button(root, text='Speak', bg='light blue', fg='black', width=8, activebackground='light green',command=recognize)
speak.place(x=425, y=50)

clear = Button(root, text='Clear', bg='gold', fg='black', activebackground='pink',width=8,command=clear)
clear.place(x=425, y=20)


root.mainloop()