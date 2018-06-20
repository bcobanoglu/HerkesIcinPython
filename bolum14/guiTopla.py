from tkinter import *
#import tkinter.messagebox as msj
gui = Tk()
global s1
s1 = StringVar()
global s2
s2 = StringVar()
#global msj
def mesaj ():#olay gerçekleşince çalışacak kod
    a = float(s1.get())
    b = float(s2.get())
    Label(gui, text=a+b).grid(row=2, column=1)
    #msj.showinfo("", "Toplam={}".format(a + b))
  
Label(gui, text="1. Sayı").grid(row=0, sticky=W)
Label(gui, text="2. Sayı").grid(row=1, sticky=W)
Button(gui,text="Toplam", command=mesaj).grid(row=2, sticky=W)
Entry(gui, textvariable=s1).grid(row=0, column=1, sticky=E)
Entry(gui, textvariable=s2).grid(row=1, column=1, sticky=E)

gui.mainloop()
