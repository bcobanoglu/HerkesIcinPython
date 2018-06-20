'''
Örnek 14.16. Spinbox Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui = Tk()
gui.title("ZikirMatik")
sayac =IntVar()
lb=Label(gui, text="Tesbihat")
lb.grid(column=0,row=0)
#spinbox değeri 33 olunca sıfırla ve etikete 'bitti' yaz
def spinAt():
    lb.config(text='Tesbihat')
    if sayac.get()==33:
        sayac.set(0)
        lb['text'] = 'bitti' #lb.config(text='bitti')
#spinbox nesnesi ve yerleşim şekli
spin=Spinbox(gui,from_=0,to=33,width=10,bd=5,textvariable=sayac, command=spinAt)
spin.grid(column=1,row=0)

#main metodu çağır
gui.mainloop()
