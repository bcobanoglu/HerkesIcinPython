'''
Örnek 14.7. Button ve Entry Uygulaması- Hesap Makinesi
@author:Bülent Çobanoğlu
'''
#gerekli modüller çağrıldı
from tkinter import *
from tkinter.font import BOLD
gui = Tk()#gui isminde Tk() nesnesi tanımlandı
gui.title("Hesap Makinesi") #çerçeve başlığı belirlendi
gui.resizable(0, 0) #çerçeve sabitlendi
snc = "" #sonuc değişkeni
sayi = StringVar()
sayi.set("Sıfırlamak için CE'ye bas!)")
hesapla = Entry(gui, textvariable = sayi) #text buton nesnesi
hesapla.grid(row=2, columnspan=10)
#sayı butonlarına basma olayının metodu
def btnBas(num):
    global snc
    snc = snc + str(num)
    sayi.set(snc)
#eşittire basma olayının metodu
def EsitrBas():
    global snc
    total = str(eval(snc))
    sayi.set(total)
#CE (Temizle) butonuna basma olayının metodu
def CEBas():
    global snc
    snc =""
    sayi.set("")
#çerçeve üzerindeki butonlar ve tıklama durumunda gerçekleşecek olaylar
Btn0 = Button(gui, text="0", command = lambda:btnBas(0))
Btn0.grid(row = 6, column = 2, padx=10, pady=10)
Btn1 = Button(gui, text="1", command = lambda:btnBas(1))
Btn1.grid(row = 3, column = 1, padx=10, pady=10)
Btn2 = Button(gui, text="2", command = lambda:btnBas(2))
Btn2.grid(row = 3, column = 2, padx=10, pady=10)
Btn3 = Button(gui, text="3", command = lambda:btnBas(3))
Btn3.grid(row = 3, column = 3, padx=10, pady=10)
Btn4 = Button(gui, text="4", command = lambda:btnBas(4))
Btn4.grid(row = 4, column = 1, padx=10, pady=10)
Btn5 = Button(gui, text="5", command = lambda:btnBas(5))
Btn5.grid(row = 4, column = 2, padx=10, pady=10)
Btn6 = Button(gui, text="6", command = lambda:btnBas(6))
Btn6.grid(row = 4, column = 3, padx=10, pady=10)
Btn7 = Button(gui, text="7", command = lambda:btnBas(7))
Btn7.grid(row = 5, column = 1, padx=10, pady=10)
Btn8 = Button(gui, text="8", command = lambda:btnBas(8))
Btn8.grid(row = 5, column = 2, padx=10, pady=10)
Btn9 = Button(gui, text="9", command = lambda:btnBas(9))
Btn9.grid(row = 5, column = 3, padx=10, pady=10)
btnTop = Button(gui, text="+", command = lambda:btnBas("+"),font=BOLD)
btnTop.grid(row = 3, column = 4, padx=10, pady=10)
btnEks = Button(gui, text="-", command = lambda:btnBas("-"),font=BOLD)
btnEks.grid(row = 4, column = 4, padx=10, pady=10)
btnCarp = Button(gui, text="*", command = lambda:btnBas("*"),font=BOLD)
btnCarp.grid(row = 5, column = 4, padx=10, pady=10)
btnBol= Button(gui, text="/", command = lambda:btnBas("/"),font=BOLD)
btnBol.grid(row = 6, column = 4, padx=10, pady=10)
#lambda fonksiyonu sadece yazıldığı satırda aktif olan kodu üretir.
btnEst= Button(gui, text="=", command = EsitrBas)
btnEst.grid(row=6, column=3, padx=10, pady=10)
btnCE = Button(gui, text="CE", command = CEBas)
btnCE.grid(row = 6, column = 1, padx=10, pady=10)
gui.mainloop()
