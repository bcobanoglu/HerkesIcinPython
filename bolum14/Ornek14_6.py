'''
Örnek 14.6.  Combobox Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
from tkinter.ttk import Combobox
gui=Tk() #gui isminde Tk() nesnesi tanımlandı
gui.title("Günler") #çerçeve başlığı

def sec(self): #sec() fonksiyonu tanımlandı
    #Eğer seçilen gün değeri 6 veya 7 ise ‘tatil’
    if box.get()=='6' or box.get()=='7':
        btn.configure(text=box.get()+".gün: Tatil")
    else: #Değilse ‘iş günü’ dür.
        btn.configure(text=box.get()+".gün: İş günü")
#label eklendi
Label(gui, text="Seçiminiz").grid(row=0, column=0)

#Combobox eklendi
box=Combobox(gui,width=15)
box.grid(column=0, row=1) #combobox yerleşim şekli
#combobox değerleri girildi
box['values'] = ('1','2','3','4','5','6','7')
box.focus() #combobox'a odaklan
#Combobox'tan birşey seçildiğinde ‘sec’ metodu çalışşın
box.bind('<<ComboboxSelected>>', sec)

#arka fontu:siyah, ön fontu:beyaz olan buton eklendi
btn=Button(gui,text="Gün",fg='white', bg='black')
btn.grid(column=1,row=1) #buton yerleşim şekli

gui.mainloop()#Olay yakalama döngüsünü başlat
