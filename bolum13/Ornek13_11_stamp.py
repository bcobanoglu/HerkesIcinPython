#author:bülent çobanoğlu
#damga ile 9 sarmalı çizer
from turtle import *
shape("circle")
penup() #kalemi kaldır

for i in range(45,-1, -1):
    stamp() #mevcut damgayı bas
    right(i) #sağa dön
    backward(15) #15 birim geri git
