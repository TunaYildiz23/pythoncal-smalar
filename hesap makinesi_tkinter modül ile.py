from tkinter import*
import tkinter
import math

def ekle(gelen):
    icerik=giris.get()+gelen
    giris.delete(0,END)
    giris.insert(0,icerik)
    return icerik
def sil():
    giris.delete(0,END)

s1=0
def islemler(islem):
    global yapılacakislem
    global s1
    s1=giris.get()
    yapılacakislem=islem
    giris.delete(0,"end")
    print(yapılacakislem)
    print(s1)
   
def hesap(esit):
    if yapılacakislem=="+":
        s2=giris.get()
        sonuc=float(s1)+float(s2)
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    elif yapılacakislem=="-":
        s2=giris.get()
        sonuc=float(s1)-float(s2)
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    elif yapılacakislem=="*":
        s2=giris.get()
        sonuc=float(s1)*float(s2)
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    
    elif yapılacakislem=="/":
        s2=giris.get()
        if s2=="0":
            giris.delete(0,"end")
            giris.insert(0,"tanımsız")
        else:
           sonuc=float(s1)/float(s2)
           giris.delete(0,"end")
           giris.insert(0,sonuc)
    elif yapılacakislem=="!":
        sonuc=math.factorial(int(s1))
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    elif yapılacakislem=="√":
        sonuc=math.sqrt(int(s1))
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    elif yapılacakislem=="%":
        s2=giris.get()
        sonuc=(float(s1)*float(s2))/100
        giris.delete(0,"end")
        giris.insert(0,sonuc)
    
                        
pencere=tkinter.Tk()
pencere.geometry("320x400+480+80")
pencere.title("HESAP MAKİNESİ")
pencere.config(bg="#d8bfd8")
               
giris=tkinter.Entry(font=("arial",16,"bold"),justify=RIGHT)
giris.place(x=30,y=10,width=260,height=40)
giris.insert(0,"")


silme=tkinter.Button(text="C",font=("arial",18,"bold"),bg="#00ffcf",command=sil)
silme.place(x=240,y=60,width=50,height=50)              

yedi=tkinter.Button(text="7",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("7"))
yedi.place(x=30,y=120,width=50,height=50)
sekiz=tkinter.Button(text="8",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("8"))
sekiz.place(x=100,y=120,width=50,height=50) 
dokuz=tkinter.Button(text="9",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("9"))
dokuz.place(x=170,y=120,width=50,height=50)


dort=tkinter.Button(text="4",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("4"))
dort.place(x=30,y=180,width=50,height=50)
bes=tkinter.Button(text="5",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("5"))
bes.place(x=100,y=180,width=50,height=50) 
alti=tkinter.Button(text="6",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("6"))
alti.place(x=170,y=180,width=50,height=50)


bir=tkinter.Button(text="1",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("1"))
bir.place(x=30,y=240,width=50,height=50)
iki=tkinter.Button(text="2",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("2"))
iki.place(x=100,y=240,width=50,height=50) 
uc=tkinter.Button(text="3",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("3"))
uc.place(x=170,y=240,width=50,height=50)


sifir=tkinter.Button(text="0",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("0"))
sifir.place(x=30,y=300,width=50,height=50)
nokta=tkinter.Button(text=".",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:ekle("."))
nokta.place(x=100,y=300,width=50,height=50) 

#işslemler
karekok=tkinter.Button(text="√",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("√"))
karekok.place(x=30,y=60,width=50,height=50)
faktoriyel=tkinter.Button(text="!",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("!"))
faktoriyel.place(x=100,y=60,width=50,height=50) 
esittir=tkinter.Button(text="=",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:hesap("="))
esittir.place(x=170,y=300,width=50,height=50)
arti=tkinter.Button(text="+",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("+"))
arti.place(x=240,y=300,width=50,height=50)
bolme=tkinter.Button(text="/",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("/"))
bolme.place(x=240,y=120,width=50,height=50)
carpma=tkinter.Button(text="X",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("*"))
carpma.place(x=240,y=180,width=50,height=50)
yüzde=tkinter.Button(text="%",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("%"))
yüzde.place(x=170,y=60,width=50,height=50)    
cikarma=tkinter.Button(text="-",font=("arial",18,"bold"),bg="#00ffcf",command=lambda:islemler("-"))
cikarma.place(x=240,y=240,width=50,height=50)

pencere.mainloop()
