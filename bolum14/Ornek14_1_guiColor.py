#author:Bülent Çobanoğlu
#Örnek 14.1. colorchooser Uygulaması
from tkinter import *
from tkinter.colorchooser import *
def renkAl():
    renk = askcolor()
    print ("RGB:",renk)
Button(text='Renk Seç', command=renkAl).pack()
mainloop()
