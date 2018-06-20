#author:Bülent Çobanoğlu
from turtle import *
#çizim kalemi kalınlığı
pensize(3)
def main():
    #wn:ekran değişkeni
    wn = Screen()
    #Çizim ekran boyutu
    wn.setup(300,300)
    #Koordinatı bulan fonksiyon
    def Nokta(x, y):
        goto(x,y)
    #Click olayı
    wn.onclick(Nokta)
    #olay yakalama döngüsü
    mainloop()
#ana program
main()
