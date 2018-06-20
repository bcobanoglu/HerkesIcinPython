'''
Örnek 13.17. Sonlu Durum Makinesi (Finite State Machine) Uygulaması
@author:Bülent Çobanoğlu
'''
from turtle import *
setup(250,300)#çerçeve boyutu
wn = Screen()#ekran değişkeni
wn.title("Trafik ışıkları!")
def levhaCiz():#trafik levhasını çiz
    penup()
    setpos(-50,-100)
    pendown()
    pensize(3)
    color("black", "lightgrey")
    begin_fill()#boyamaya başla
    forward(80)
    left(90)
    forward(200)
    circle(40, 180)#yarım daire çiz
    forward(200)
    left(90)
    end_fill()#boyamayı sonlandır
levhaCiz()#levhaCiz fonk. çağrıldı
penup()#kalemi kaldır
forward(40)
left(90)
forward(50)
shape("circle")#Lamba şekli
shapesize(3)
fillcolor("green")#ilk önce yeşil
trfkDurum = 0#Yeşil(0),Sarı(1),Kırmızı(2)
def durumMakinesi():
    global trfkDurum #global değişken
    if trfkDurum == 0: #0 dan 1 e geçiş
        forward(70)
        fillcolor("yellow")
        trfkDurum = 1
    elif trfkDurum == 1: #1 den 2 ye geçiş
        forward(70)
        fillcolor("red")
        trfkDurum = 2
    else: # 2 den 0 a geçiş
        back(140)
        fillcolor("green")
        trfkDurum  = 0
#Işık geçişleri için space tuşuna bas
wn.onkey(durumMakinesi, "space")
wn.listen() # Olayları dinle
