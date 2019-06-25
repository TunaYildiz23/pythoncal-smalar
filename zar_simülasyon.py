import random
import tkinter
from tkinter import Tk


def zar():
    a=random.randint(1,6)
    b=random.randint(1,6)
    
    zar1sonuc.config(text=a)
    zar2sonuc.config(text=b)
    
    
pencere=Tk()
pencere.geometry("240x240")
pencere.title("ZAR SİMİLASYON")
pencere.config(bg="yellow")



zar1=tkinter.Label(pencere,font=("arial",18,"bold"),text="1.ZAR",fg="red",bg="black")
zar1.place(x=20,y=5)

zar1sonuc=tkinter.Label(pencere,font=("arial",48,"bold"),bg="yellow")
zar1sonuc.place(x=40,y=50)

zar2=tkinter.Label(pencere,font=("arial",18,"bold"),text="2.ZAR",fg="red",bg="black")
zar2.place(x=150,y=5)

zar2sonuc=tkinter.Label(font=("arial",48,"bold"),bg="yellow")
zar2sonuc.place(x=180,y=50)


buton=tkinter.Button(pencere,text="ZAR AT",font=("arial",20,"bold"),command=zar)
buton.place(x=60,y=180)


   

pencere.mainloop()
    
