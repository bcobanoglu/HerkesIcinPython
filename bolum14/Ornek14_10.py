'''
Örnek 14.10. Radiobutton uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msj #messagebox; msj ile temsil edilecek
gui=Tk() #Tk nesnesi
gui.title("Takımını Seç!") #çerçeve başlığı
gui.geometry('200x150') #çerçeve boyutu
v = StringVar #String değişken
def secim():
    msj.showinfo("Favori takımım", message=v.get())

rb1 =Radiobutton(text='Galatasaray', variable=v, value="Aslan Cimbom", command=secim)
rb1.pack(anchor=W)
rb2 =Radiobutton(text='Beşiktaş', variable=v, value="Kara Kartal", command=secim)
rb2.pack(anchor=W)
rb3 =Radiobutton(text='Fenerbahçe', variable=v, value="Sarı Kanarya", command=secim)
rb3.pack(anchor=W)
rb4 =Radiobutton(text='Trabzon', variable=v, value="Kaplan", command=secim)
rb4.pack(anchor=W)
rb5 =Radiobutton(text='Bursa', variable=v, value="Timsahlar", command=secim)
rb5.pack(anchor=W)
gui.mainloop()
