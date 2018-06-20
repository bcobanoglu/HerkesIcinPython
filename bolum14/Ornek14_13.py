'''
Örnek 14.13. Optionmenu Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui = Tk()
gui.title("Sözlük Programı")
#Değişken tanımlamaları: deg1, deg2
deg1 = StringVar()
deg1.set("İngilizce") # başlangıç değeri
deg2 = StringVar()
deg2.set("Türkçe") # başlangıç değeri
#iki adet optionmenu tanımlanıyor
menu1 = OptionMenu(gui,deg1,"one","two","three","four")
menu1.pack(side=LEFT) #menu1 yerleşimi
menu2 = OptionMenu(gui,deg2,"bir","iki","üç","dört")
menu2.pack(side=LEFT) #menu2 yerleşimi
def cevir(): #ingilizce-türkçe çevirimi
    print (deg1.get(), "=", deg2.get())
#Buton tanımı ve yerleşimi
buton = Button(gui, text="OK", command=cevir)
buton.pack(side=LEFT)
gui.mainloop()
