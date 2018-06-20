'''
Örnek 14.15. Text ve Scrollbar Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui=Tk()
text = Text(gui, height=30, width=50) #Text nesnesi
bar = Scrollbar(gui, command=text.yview) #Scrollbar nesnesi
text.configure(yscrollcommand=bar.set) #bar hareketi ile text'i ilişkilendir
#text ayarları
text.tag_configure('bold', font=('Consolas', 11, 'bold', 'italic'))
text.tag_configure('renk', foreground='gray', font=('Papyrus', 13))
#text'e metin ekle
text.insert(END, "Ey Oğullarım!\n")
text.insert(END, 'Günlerinizi nasıl kodlarsanız,\nElbette ki!\n', )
text.insert(END, 'Bütün bir ömrünüzü de öyle kodlamış olursunuz.', 'bold')
text.insert(END, '\n...Babanız...\n', 'renk')
#text'e buton ekle
button = Button(text, text='Berat İsmail &  Levent Ekrem & Ömer Can')
text.window_create(END, window=button)
#text'e foto ekle
foto=PhotoImage(file="kale.png")
text.image_create(END, image=foto)
text.pack(side=LEFT) #text yerleşimi
bar.pack(side=RIGHT, fill=Y) #scrollbar yerleşimi
gui.mainloop()
