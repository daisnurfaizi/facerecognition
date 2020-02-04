import cv2
import numpy as np 
import sqlite3
import os
#from pygame import mixer
import time
from tkinter import *
import tkinter.messagebox
import subprocess
os.system('python3 create_database.py')
conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')
root=Tk()
root.geometry('300x370')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Rekam Wajah')
frame.config(background='light blue')
label = Label(frame, text="Rekam Wajah",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)
textin=StringVar()
textinn=StringVar()
def hel():
    help(cv2)
 
def Contri():
    tkinter.messagebox.showinfo("Contributors","Dais")
 
 
def anotherWin():
    tkinter.messagebox.showinfo("About",'Aplikasi Rekam Wajah v1.0\n dibuat dengan\n-OpenCV\n-Numpy\n-Tkinter\n di Python 3')
                                     
    
 
menu = Menu(root)
root.config(menu=menu)
 
subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Doc",command=hel)
 
subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Rekam Wajah",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)
 
def exitt():
    exit()
   #exec(open("security.py").read())
def security():
    exec(open("train.py").read())
    cv2.destroyAllWindows()
   
def insert():
    c = conn.cursor()

    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    name1 = textin.get()
    #membuat path
    if not os.path.exists('./dataset/'+name1):
      os.makedirs('./dataset/'+name1)
    

    c.execute('INSERT INTO users (name) VALUES (?)', (name1,))

    uid = c.lastrowid

    sampleNum = 0
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
          sampleNum = sampleNum+1
          cv2.imwrite("dataset/"+name1+"/User."+str(uid)+"."+str(sampleNum)+".jpg",img[y:y+h,x:x+w])
          cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
          cv2.waitKey(100)
        cv2.imshow('img',img)
        cv2.waitKey(1)
        if sampleNum > 20:
          break
    cap.release()
      
    conn.commit()
      
    conn.close()
    cv2.destroyAllWindows()
    exec(open("train.py").read())
lab=Label(root,text='Nama:',font=('none 13 bold'))
lab.place(x=5,y=104)

entname=Entry(root,width=15,font=('none 13 bold'),textvar=textin)
entname.place(x=100,y=104)
but1=Button(frame,padx=5,pady=5,width=15,bg='white',fg='black',relief=GROOVE,command=insert,text='Rekam Wajah',font=('helvetica 10 bold'))
but1.place(x=100,y=130)

#but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
#but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=18,bg='white',fg='black',relief=GROOVE,command=security,text='Training Data',font=('helvetica 15 bold'))
but3.place(x=5,y=160)

#but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
#but4.place(x=5,y=322)

#but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
#but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=18,bg='white',fg='black',relief=GROOVE,text='Keluar',command=exitt,font=('helvetica 15 bold'))
but5.place(x=5,y=200)


root.mainloop()
subprocess.run(["python3", "kamera.py"])
