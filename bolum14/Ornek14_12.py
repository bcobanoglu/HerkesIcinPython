'''
Örnek 14.12. Listbox Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui = Tk()
gui.title("Sözlük Programı")
#Listbox-1 nesnesi tanımlandı ve yerleştirildi
lBox1 = Listbox(gui)
lBox1.grid(row=0,column=0)
#Listbox-2 nesnesi tanımlandı ve yerleştirildi
lBox2 = Listbox(gui)
lBox2.grid(row=0,column=1)
#lBox1 nesnesine elemanlar eklendi
lBox1.insert(END, "İngilizce")
eng=["one", "two", "three", "four", "five"]
for item in eng:
    lBox1.insert(END, item)
#lBox2 nesnesine elemanlar eklendi
lBox2.insert(END, "Türkçe")
trk=["bir", "iki", "üç", "dört", "beş"]
for item in trk:
    lBox2.insert(END, item)
gui.mainloop()
