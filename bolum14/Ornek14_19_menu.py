'''
Örnek 14.19. Menu Uygulaması:
@author:Bülent Çobanoğlu
'''
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msj #messagebox'ı import et
gui=Tk() #Tk nesnesi
#Menü nesneleri seçildiğinde çalışacak fonksiyonlar
def islem():
    pencere = Toplevel(gui) #En üst pencere
    btn = Menubutton(pencere, text="Test butonu")
    btn.pack()
def mesaj():
    msj.showinfo(title="Hakkında", message="Bülent Çobanoğlu")

menuNesnesi = Menu(gui) #menü nesnesi oluşturuldu
#Dosya menüsü
dosyaMenu = Menu(menuNesnesi, tearoff=0)
dosyaMenu.add_command(label="Yeni",accelerator='Ctrl+N', command=islem)
dosyaMenu.add_command(label="Aç", command=islem)
dosyaMenu.add_command(label="Kaydet", command=islem)
dosyaMenu.add_command(label="Farklı Kaydet", command=islem)
dosyaMenu.add_command(label="Kapat", command=islem)
dosyaMenu.add_separator() #ayıraç çizgisi ekle
dosyaMenu.add_command(label="Çıkış", command=gui.quit)
menuNesnesi.add_cascade(label="Dosya", menu=dosyaMenu) #Dosya üst menüsü
#Düzen menüsü
duzenMenu = Menu(menuNesnesi, tearoff=0)
duzenMenu.add_command(label="Geri", command=islem)
duzenMenu.add_separator() #ayıraç çizgisi ekle
duzenMenu.add_command(label="Kes", accelerator='Ctrl+X',command=islem)
duzenMenu.add_command(label="Kopyala", accelerator='Ctrl+C', command=islem)
duzenMenu.add_command(label="Yapıştır", accelerator='Ctrl+V', command=islem)
duzenMenu.add_command(label="Sil", command=islem)
menuNesnesi.add_cascade(label="Düzen", menu=duzenMenu) #Düzen üst menüsü
#Yardım menüsü
helpMenu = Menu(menuNesnesi, tearoff=0)
helpMenu.add_command(label="Yardım içeriği", command=islem)
helpMenu.add_command(label="Hakkında...", command=mesaj)
menuNesnesi.add_cascade(label="Yardım", menu=helpMenu) #Yardım üst menüsü

gui.config(menu=menuNesnesi) #grafik ekrana menüyü yerleştir.
gui.mainloop()
