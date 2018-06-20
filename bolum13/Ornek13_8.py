#author:Bülent Çobanoğlu
#İç içe 3 adet kare çizimi
from turtle import *
shape('blank') #Ok kullanma
begin_fill() #boyamaya başla
pensize(3) #çizgi kalınlığı

for renk in ["red", "green", "blue", "black"]:
   pencolor(renk) #çizgi rengi
   forward(50)
   left(90)

for renk in ["red", "green", "blue", "black"]:
   pencolor(renk)
   forward(100)
   left(90)

for renk in ["red", "green", "blue", "black"]:
   pencolor(renk)
   forward(150)
   left(90)

fillcolor("lightgray") #dolgu rengi: açık gri
end_fill() #boyamayı sonlandır
