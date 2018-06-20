'''
Örnek 14.14. PanedWindow Uygulaması
@author:Bülent Çobanoğlu
'''
from tkinter import *
gui=Tk()
#ilk pencere açıldı
p1 = PanedWindow()
p1.pack(fill=BOTH, expand=1)
#sola label nesnesi eklendi
sol = Label(p1, text="Sol panel")
p1.add(sol)
#ikinci pencere açıldı
p2 = PanedWindow(p1, orient=VERTICAL)
p1.add(p2)
#Üste arka fontu beyaz Buton nesnesi eklendi
ust = Button(p2, text="Üst panel",fg="black",bg="white")
p2.add(ust)
#Alta arka fontu siyah Buton nesnesi eklendi
alt = Button(p2, text="Alt panel",fg="white",bg="black")
p2.add(alt)
#Üçüncü pencere açıldı
p3 = PanedWindow(p1, orient=VERTICAL)
p1.add(p3)
#Sağa Scrollbar nesnesi eklendi
sag = Scrollbar(gui)
p3.add(sag)

gui.mainloop()
