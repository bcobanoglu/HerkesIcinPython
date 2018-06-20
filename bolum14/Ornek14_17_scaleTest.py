'''
Örnek 14.17. Scale Uygulaması
@author:Bülend Hoca
'''
from tkinter import *

def yazDegeri(value=None):
    print (s1.get(), s2.get())

gui=Tk()
s1 = Scale(gui, from_=6, to=0, resolution=0.5, command=yazDegeri)
s1.place(x=0,y=15)
s1.set(5.0)
s2 = Scale(gui, from_=0, to=10, orient=HORIZONTAL,command=yazDegeri)
s2.place(x=20,y=100)
Button(gui, text='Koordinat', command=yazDegeri).place(x=75,y=150)
gui.mainloop()
