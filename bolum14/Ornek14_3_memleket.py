#author:Bülent Çobanoğlu
#Örnek 14.3. ScrolledText Uygulaması
from tkinter import *
import tkinter.scrolledtext
gui= Tk()
#ScrolledText, st ile temsil edilecek
st = tkinter.scrolledtext.ScrolledText(gui)
st.pack() #yerleşim metodu

#metin (şiir) eklendi
st.insert(INSERT,
"""\
Memleket isterim
Gök mavi, dal yeşil, tarla sarı olsun;
Kuşların çiçeklerin diyarı olsun.

Memleket isterim
Ne başta dert, ne gönülde hasret olsun;
Kardeş kavgasına bir nihayet olsun.

Memleket isterim
Ne zengin fakir, ne sen ben farkı olsun;
Kış günü herkesin evi barkı olsun.

Memleket isterim
Yaşamak, sevmek gibi gönülden olsun;
Olursa bir şikâyet ölümden olsun.
""")
st.insert(END, "Cahit Sıtkı Tarancı")
''' st bileşenindeki metni 1. satırından son (END)satırına kadar konsol ekrana yaz'''
print( st.get(1.0, END) )
gui.mainloop() #olay yakalama döngüsü
