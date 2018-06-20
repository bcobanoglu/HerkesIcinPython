#Örnek 14.18. Canvas Uygulaması
#author:Bülend Hoca
from tkinter import *
gui=Tk()
gui.title("Çizim tuvalı")
tuval = Canvas(gui, width =350, height=350)#Canvas(tuval) boyutu
tuval.create_oval(10,10,100,100, fill='gray30') #daire
tuval.create_line(100,90,200,90) #çizgi
tuval.create_rectangle(200,10,250,60, outline='black', fill='gray60')#kare
tuval.create_polygon(205,110,285,125,160,175,210,200, fill='black') #Poligon
tuval.create_bitmap(200, 280, bitmap='info') #ikon/simge
xy = 10, 105, 100, 200
tuval.create_arc(xy, start=0, extent=270, fill='gray90') #yay
tuval.create_text(250,220, text='Python', font=('consolas', 26)) #yazı
#çerçeve çizilip, içine buton yerleştirildi
frm = Frame(tuval, relief=GROOVE, borderwidth=3) #çerçeve
Button(frm, text="Tuvalim").pack() #buton yerleşimi
tuval.create_window(250, 280, window=frm, anchor='center')
tuval.pack() #canvas(tuval)yerleşimi
gui.mainloop() #ana döngü
