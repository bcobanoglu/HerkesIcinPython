'''
Örnek 14.4. simpledialog ve messagebox Uygulaması:
@author:Bülent Çobanoğlu
'''
from tkinter import *
#İmport edilen messagebox, ‘msj’ ile temsil edilecek
import tkinter.messagebox as msj
#simpledialog nesnesini import et
from tkinter import simpledialog
gui=Tk()
#pencereden girilen string ‘s’ de tutulacak
s = simpledialog.askstring("Palindrom mu?", "Kelime:",parent=gui)
#Eğer girilen string ise
if s == ''.join(reversed(s)):
    msj.showinfo(title=s, message="Evet Palindrom")
else: #değilse
    msj.showwarning(title=s, message="Palindrom Değil!")
gui.mainloop()
