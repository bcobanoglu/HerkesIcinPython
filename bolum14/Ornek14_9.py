'''
Örnek 14.9. Progressbar uygulaması-2:
@author:Bülent Çobanoğlu
'''
from tkinter import *
from tkinter.ttk import Progressbar
import time
gui=Tk() #Tk nesnesi
#progressbar tanımlandı
bar=Progressbar(gui, length=100)
#progressbar yerleşim şekli
bar.place(x=10, y=10)
#progressbar ilerleme fonksiyonu tanımlandı
def ilerle():
    #Eğer bar en son değerine ulaşırsa
    if bar['value']>bar['maximum']:
        bar['value']=1 #barı 1 birim yap
    else:
        bar['value']+=1 #barı 1 birim artır
        gui.update() #barı güncelle
        time.sleep(1) #bar ilerleme hızı
#ana program
if __name__ == '__main__':
    while(1):#sonsuz döngü içerisinde
        ilerle() #sürekli çalışacak fonksiyon
        #Yüzdelik ilerlemeyi gösteren etiket
        Label(gui,text="%"+str(bar['value'])).place(x=110, y=10)
    gui.mainloop()
