#author:Bülend Hoca
#Saat çizimi
from turtle import *
import time
title("Benim Saatim")
shape('blank')
setup(450,450)
bgcolor('black')
pensize(4)
penup()
pencolor('white')
saat=0
for i in range(12):
    saat+=1
    penup()
    setheading(-30*i+60)
    forward(150)
    pendown()
    forward(25)
    penup()
    forward(20)
    write(str(saat),align="center",\
          font=("Consolas", 11))
    if saat==12:
        saat=0
    home()
penup()
setpos(-75,0)
pendown()
pencolor('white')
#C dili tarzı zaman fonksiyonunu yaz
write(str(time.ctime()),\
      font=("Arial", 11))
