'''
Örnek 14.2. simpledialog uygulaması
@author:Bülent Çobanoğlu
'''
import tkinter as tk #tkinter, tk ile temsil edilecek
from tkinter import simpledialog #simpledialog nesnesini import et
gui = tk.Tk() #gui isminde tk(tkinter) nesnesi oluşturuldu

cvp = simpledialog.askstring("Input", "Adınız?",parent=gui)
#Eğer girilen değer string ise
if cvp is not None:
    print("Adınız..: ", cvp) #girileni yaz
else:#değilse
    print("Lütfen adı düzgün giriniz!") #uyar!

cvp = simpledialog.askinteger("Input", "Yaşınız?",
                                 parent=gui, minvalue=0, maxvalue=100)
#Eğer girilen değer integer ise
if cvp is not None:
    print("Yaşınız..: ", cvp) #girileni yaz
else: #değilse
    print("Lütfen yaşı düzgün giriniz!") #uyar!
