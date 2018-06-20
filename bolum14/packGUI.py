from tkinter import *
gui = Tk()
#Label çerçeve ortasına yerleşti
Label(gui, text="Pack metodu örneği").pack()
#Başlık genişliğinde çerçeve ortasına yerleşti
Button(gui, text="genişlet bakalım").pack(expand = 1)
#A butonu Y ekseninde uzatıldı ve sola yerleşti
Button(gui, text="A").pack(side=LEFT, fill=Y)
#B butonu X ekseninde uzatıldı ve yukarı yerleşti
Button(gui, text="B").pack(side=TOP, fill=X)
#C butonu uzatılmadan sağa yerleşti
Button(gui, text="C").pack(side=RIGHT, fill=NONE)
#D butonu her iki yana uzatıldı ve aşağı yerleşti
Button(gui, text="D").pack(side=BOTTOM, fill=BOTH)
gui.mainloop()


