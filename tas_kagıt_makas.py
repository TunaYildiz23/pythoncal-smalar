import tkinter
import random


def tas_kagıt_makas():
    liste=["tas","kagıt","makas"]
    oyuncu_1=random.choice(liste)
    oyuncu_2=random.choice(liste)
    print(oyuncu_1,oyuncu_2)
    kisi_bir_sonuc.config(text=oyuncu_1)
    kisi_iki_sonuc.config(text=oyuncu_2)


    if oyuncu_1=="tas" and oyuncu_2=="makas":
        sonuc.config(text="1.oyuncu kazandı")
    elif oyuncu_1=="makas" and oyuncu_2=="tas":
        sonuc.config(text="2.oyuncu kazandı")
    
    elif oyuncu_1=="makas" and oyuncu_2=="kagıt":
        sonuc.config(text="1.oyuncu kazandı")
    elif oyuncu_1=="kagıt" and oyuncu_2=="makas":
        sonuc.config(text="2.oyuncu kazandı")
    
    elif oyuncu_1=="kagıt" and oyuncu_2=="tas":
        sonuc.config(text="1.oyuncu kazandı")
    elif oyuncu_1=="tas" and oyuncu_2=="kagıt":
        sonuc.config(text="2.oyuncu kazandı")

    else:
         sonuc.config(text="oyun berabere biter")


pencere=tkinter.Tk()
pencere.geometry("480x360")
pencere.title("TAS KAGIT MAKAS")
pencere.config(bg="DarkSlateGray2")

kisi_bir=tkinter.Label(text="1.OYUNCU",fg="red",bg="yellow")
kisi_bir.grid(padx=20,pady=5)

kisi_bir_sonuc=tkinter.Label(text="",bg="white",width=10,height=2)
kisi_bir_sonuc.grid(padx=20,pady=15)


kisi_iki=tkinter.Label(text="2.OYUNCU",fg="red",bg="yellow")
kisi_iki.grid(padx=20,pady=5)


kisi_iki_sonuc=tkinter.Label(text="",bg="white",width=10,height=2)
kisi_iki_sonuc.grid(padx=20,pady=25)

sonuc=tkinter.Label(text="kazanan",bg="yellow",font=("arial",16,"bold"))
sonuc.place(x=200,y=100)


lbl=tkinter.Button(pencere, text='OYNA', fg='white',   bg='purple', font=('comicsans', 12),command=tas_kagıt_makas)
lbl.grid(padx=40,pady=30)


pencere.mainloop()
