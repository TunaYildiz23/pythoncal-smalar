import tkinter
from tkinter import*
from tkinter.ttk import Combobox
import sqlite3


def save():
    ad=adgiris.get()
    soyad=soyadigiris.get()
    kimlikNo=tcNogiris.get()
    Cinsiyeti=Cinsiyetgiris.get()
    day=gun.get()
    mount=ay.get()
    year=yil.get()
    tlf=telefon.get()
    isim="Adi               :"+ad
    soyisim="Soyadı        :"+soyad
    kimlik="T.C No         :"+kimlikNo
    cinsiyeti="Cinsiyeti     :"+Cinsiyeti
    D_Tarih="D.Tarihi       :"+day+"/"+mount+"/"+year
    tl_f="Telefon No :"+tlf
    D_Tarih1=day+"/"+mount+"/"+year
    
    if kimlikNo.isdigit()==False or tlf.isdigit()==False:
        yazi7.config(text="T.C kimlik numaranız veya \n telefon nuraranızda harf kullanmayınız")
        telefon.delete(0,END)
        tcNogiris.delete(0,END)
    else:
        import sqlite3
        baglan=sqlite3.connect("kayıtFormu.db")
        cursor=baglan.cursor()
        cursor.execute("create table IF NOT EXISTS kayıtFormu (Adı text,Soyadı Text,T_C No text,Cinsiyet text,D Tarih text,Telefon int)")
        cursor.execute("insert into kayıtFormu values(?,?,?,?,?,?)",(ad,soyad,kimlikNo,Cinsiyeti,D_Tarih1,tlf))
        baglan.commit()
        baglan.close()


        yazi1.config(text=isim)
        yazi2.config(text=soyisim)
        yazi3.config(text=kimlik)
        yazi4.config(text=cinsiyeti)
        yazi5.config(text=D_Tarih)
        yazi6.config(text=tl_f)
        yazi7.config(text="")
        adgiris.delete(0,END)
        soyadigiris.delete(0,END)
        tcNogiris.delete(0,END)
        Cinsiyetgiris.delete(0,END)
        gun.delete(0,END)
        ay.delete(0,END)
        yil.delete(0,END)
        telefon.delete(0,END)
        

        



   

  

window=tkinter.Tk()
window.geometry("720x480")

#text kısmı
adi=Label(window,text="Adı",font=("arial",12,"bold")).place(x=10,y=10)
soyadi=Label(window,text="Soyadı",font=("arial",12,"bold")).place(x=10,y=40)
tcNo=Label(window,text="T.C No",font=("arial",12,"bold")).place(x=10,y=70)
cinsiyet=Label(window,text="Cinsiyet",font=("arial",12,"bold")).place(x=10,y=100)
dogumTarihi=Label(window,text="D.Tarihi",font=("arial",12,"bold")).place(x=10,y=130)
telefon=Label(window,text="Tlf No",font=("arial",12,"bold")).place(x=10,y=160)


yazi1=Label(window,font=("arial",12,"bold"))
yazi1.place(x=10,y=240)
yazi2=Label(window,font=("arial",12,"bold"))
yazi2.place(x=10,y=270)
yazi3=Label(window,font=("arial",12,"bold"))
yazi3.place(x=10,y=300)
yazi4=Label(window,font=("arial",12,"bold"))
yazi4.place(x=10,y=330)
yazi5=Label(window,font=("arial",12,"bold"))
yazi5.place(x=10,y=360)
yazi6=Label(window,font=("arial",12,"bold"))
yazi6.place(x=10,y=390)
yazi7=Label(window,font=("arial",12,"bold"),fg="red")
yazi7.place(x=250,y=200)






#giris kısımları
adgiris=Entry(window,width="23",fg="blue",font=("arial",8,"bold"))
adgiris.place(x=100,y=10)
soyadigiris=Entry(window,width="23",fg="blue",font=("arial",8,"bold"))
soyadigiris.place(x=100,y=40)
tcNogiris=Entry(window,width="23",fg="blue",font=("arial",8,"bold"))
tcNogiris.place(x=100,y=70)
secenek=["Erkek","Kız"]
Cinsiyetgiris=Combobox(window,value=secenek,)
Cinsiyetgiris.place(x=100,y=100)
gun=Spinbox(window,from_=1, to=30, width=5,fg="blue",font=("arial",8,"bold"))
gun.place(x=100,y=130)
ay=Spinbox(window,from_=1, to=12, width=5,fg="blue",font=("arial",8,"bold"))
ay.place(x=147,y=130)
yil=Spinbox(window,from_=1950, to=2005, width=5,fg="blue",font=("arial",8,"bold"))
yil.place(x=195,y=130)
telefon=Entry(window,width="23",fg="blue",font=("arial",8,"bold"))
telefon.place(x=100,y=160)



#buton kısımları
kaydet=Button(window,text="KAYDET",font=("arial",20,"bold"),bg="#FFA500")
kaydet.config(command=save)
kaydet.place(x=270,y=60)

window.mainloop()