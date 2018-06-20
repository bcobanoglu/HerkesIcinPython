#tkinter metotlarını programa import et
from tkinter import *
#colorchooser metotlarını programa import et
from tkinter.colorchooser import *
#renkAl() metodu/fonksiyonu tanımlandı
def renkAl():
    renk = askcolor() #colorchooser'dan renk seç
    print ("RGB= %.2f" %renk) #seçilen rengi ekrana yaz
    
#Buton nesnesinin etiketini "Renk Seç" olarak belirle 
#ve butona tıklandığında renkAl() fonksiyonunu çalıştır 
Button(text='Renk Seç', command=renkAl).pack()
#grafik ekran olay yakalama ana döngüsünü çalıştır
mainloop()
