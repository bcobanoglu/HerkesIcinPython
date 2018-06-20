from tkinter import *
root = Tk()
#Kullanıcı Adı etiketi 0.satır ve batı(W)'da
Label(root, text="Kullancı Adı").grid(row=0, sticky=W)
#Sifre etiketi 1. satır ve batı(W)'da
Label(root, text="Sifre").grid(row=1, sticky=W)
#Veri giriş kutusu 0. satır, 1. sütun ve doğu(E)'da
Entry(root).grid(row=0, column=1, sticky=E)
#Veri giriş kutusu 1. satır, 1. sütun ve doğu(E)'da
Entry(root).grid(row=1, column=1, sticky=E)
#Giriş butonu 2. satır, 1. sütun ve kuzey-batı(NW)'da
Button(root, text="Giris").grid(row=2, column=1, sticky=NW)
root.mainloop()
