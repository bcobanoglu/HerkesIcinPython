'''
Örnek 14.5. Label ve Entry Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui = Tk()
global s1 #global değişken
s1 = StringVar()
global s2 #global değişken
s2 = StringVar()
#butona tıklama olayı gerçekleşince çalışacak metot
def mesaj ():
    a = float(s1.get())
    b = float(s2.get())
    Label(gui, text=a+b).grid(row=2, column=1)
#Ana program
Label(gui, text="1. Sayı").grid(row=0, sticky=W)
Label(gui, text="2. Sayı").grid(row=1, sticky=W)
Button(gui,text="Toplam", command=mesaj).grid(row=2, sticky=W)
Entry(gui, textvariable=s1).grid(row=0, column=1, sticky=E)
Entry(gui, textvariable=s2).grid(row=1, column=1, sticky=E)
gui.mainloop() #Olay yakalama döngüsü
