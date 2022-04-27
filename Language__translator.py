from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from langdetect import detect
from gtts import gTTS 
import os
import speech_recognition as sr
import codecs
import codecs



root=Tk()
root.title("Madhan translator")
root.geometry("1080x800")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    c4=combo3.get()
    c5=combo4.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    label3.configure(text=c4)
    label4.configure(text=c5)
    root.after(1000,label_change)

def translate_now():  #translateNow()
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        translator = Translator()
        translation = translator.translate(text_, dest=c3)
        text2.delete(1.0,END)
        text2.insert(END,translation.text) 
       
        
            # Words to voice
        my_te=text2.get(1.0 , END)
        lan=detect(my_te)
        myobj = gTTS(text=my_te, lang=lan, slow=False) 
        myobj.save("output.mp3") 
        os.system("start output.mp3") 



    except Exception as e:
         messagebox.showerror("googletrans",e)
         print(e)


def spe_now():
    global language
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        print("I heard  !!!")
    try:
        global language
        text = r.recognize_google (audio , language="en")
        print("You said :" , text)
        try:
            text_=text
            c6=combo3.get()
            c7=combo4.get()
            translator = Translator()
            translation = translator.translate(text_, dest=c7)
            text3.delete(1.0,END)
            text3.insert(END,translation.text)

            # Words to voice
            
            my_te=text3.get(1.0 , END)
            lan=detect(my_te)
            myobj = gTTS(text=my_te, lang=lan, slow=False) 
            myobj.save("output.mp3") 
            os.system("start output.mp3")
        except:
             print("sorry could not convert to audio")
 

    except sr.UnknownValueError:
        print("Sorry could not recognize what you said")

#speaker
sp_image=r"C:\Users\91630\Downloads\speaker.png"
sp_image_for_button = PhotoImage(file=sp_image)


#icon
img_icon=PhotoImage(file=r"C:\Users\91630\Downloads\arrow (1).png")
root.iconphoto(False,img_icon)


#arrow
arrow_image=PhotoImage(file=r"C:\Users\91630\Downloads\arrow (1).png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)



language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("english")



label1=Label(root,text="ENGLISH",font="segoe 23 bold",bg="white",width=14,bd=5,relief=GROOVE)
label1.place(x=90,y=50)

#*
f=Frame(root,bg="blue",bd=5)
f.place(x=10,y=118,width=440,height=210)
text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("select language")

label2=Label(root,text="ENGLISH",font="segoe 23 bold",bg="white",width=14,bd=5,relief=GROOVE)
label2.place(x=710,y=50)

#*pipp
f1=Frame(root,bg="Green",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate buttons
translate=Button(root,text="Translate through text and voice",font="Roboto 15 bold italic",
                 activebackground="purple",cursor="hand2",bd=5,
                 bg="blue",fg="white",command=translate_now)
translate.place(x=370,y=350)


# voice to speech

combo3=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo3.place(x=110,y=400)
combo3.set("select language")

combo4=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo4.place(x=730,y=400)
combo4.set("select language")

f2=Frame(root,bg="black",bd=5)
f2.place(x=620,y=500,width=440,height=210)

label3=Label(root,text="ENGLISH",font="segoe 23 bold",bg="white",width=14,bd=5,relief=GROOVE)
label3.place(x=90, y=430)

label4=Label(root,text="ENGLISH",font="segoe 23 bold",bg="white",width=14,bd=5,relief=GROOVE)
label4.place(x=710,y=430)

text3=Text(f2,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text3.place(x=0,y=0,width=430,height=200)

scrollbar3=Scrollbar(f2)
scrollbar3.pack(side="right",fill="y")

scrollbar3.configure(command=text3.yview)
text3.configure(yscrollcommand=scrollbar3.set)

label5=Label(root,text="Tap speaker to speak",font="segoe 23 bold",bg="white",width=17,bd=5,relief=GROOVE)
label5.place(x=60, y=510)

speech=Button(root,image=sp_image_for_button  ,command=spe_now, height=34 , width=34)
speech.place(x=400 , y=510 )

label_change()

root.configure(bg="white")
root.mainloop()
