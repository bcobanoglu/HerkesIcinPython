'''
Örnek 14.8. Progressbar uygulaması-1:
@author:Bülent Çobanoğlu
'''
from tkinter import *
from tkinter.ttk import *
import time
gui=Tk() #Tk nesnesi
#progressbar tanımlandı
bar=Progressbar(gui,length=100)
#progressbar yerleşimi:çerçeve genişliğinde uzat
bar.pack(expand="yes", fill="both")
#progressbar ilerleme fonksiyonu tanımlandı
def ilerle():
    for i in [25,50,75,100]:
        bar['value']=i #bar değerleri
        gui.update() #barı güncelle
        time.sleep(1) #bar ilerleme hızı
#Butona basılınca ilerleme başlayacak
Button(gui,text='Başla',command=ilerle).pack()
gui.mainloop()
