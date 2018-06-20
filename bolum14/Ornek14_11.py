'''
Örnek 14.11. Checkbutton-Label uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui=Tk()
cVar =IntVar()
#checkbutonun seçili olup/olmamasına göre çalışacak fonksiyon
def cBtnSec():
    if cVar.get() == 1: #checkbox seçildi ise '1' değilse '0'
        Label(gui, text="Arial kırmızı font.", font="Arial", fg="Red").pack()
    else:
        Label(gui, text="Varsayılan font", font="default").pack()

cBtn =Checkbutton(text="Arial ve Kırmızı", variable=cVar, command=cBtnSec)
cBtn.deselect() #Checkbox başlangıçta seçili olmasın
cBtn.pack(fill="both", expand=1) #checkbox yerleşim şekli
gui.mainloop()
