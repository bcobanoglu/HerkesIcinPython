#Çokgen çizimi
#author:Bülent Çobanoğlu
from turtle import *
kenar= int(textinput("", "Kenar sayısı:"))
aci = 360/kenar
pensize(2)
for i in range(kenar):
    circle (50, aci, 1)
