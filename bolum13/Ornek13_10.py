#author:Bülent Çobanoğlu
#japon bayrağı
from turtle import *
shape('blank')
pensize(5) #kalın çerçeve
#dikdörtgen çerçeveyi çizelim
for i in range(2):
  forward(150)
  right(90)
  forward(100)
  right(90)

pensize(1) #kalem kalınlığı
pencolor("red") #kalem rengi

penup() #kalemi kaldır
goto (75,-80) #daire pozisyonu
pendown()#kalemi koy
#daire çizip, kırmızıya boya
fillcolor("red")
begin_fill() #boyama başla
circle(30) #yarıçapı:30
end_fill() #boyamayı bitir
