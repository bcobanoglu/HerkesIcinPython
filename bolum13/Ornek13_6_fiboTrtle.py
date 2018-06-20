#author:Bulend Hoca
from turtle import *
#fibonacci serisi
fibN = [1,1,2,3, 5, 8, 13, 21, 34,55]
#seri eleman sayısı
uz=len(fibN)
k=5 #genişletme katsayısı
pensize(2)#kalem kalınlğı
#kare şeklinde odalar
def kareCiz(kenarUz):
   for i in range (6):
       forward(kenarUz)
       right(90)

#9 gözlü ev planı
for i in range(uz-1):
   left(90)
   kareCiz(fibN[i]*k)
