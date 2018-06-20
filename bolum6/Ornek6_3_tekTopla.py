'''
Örnek 6.3.
1’den 100 e kadar olan tek sayıların toplamını bulan programı kodlayınız.
'''
# -*- coding: UTF-8 -*-
a=1
Top=0 #Yığmalı Toplama değişkeni
while a <= 100:
    Top=Top+a #Yığmalı toplama
    a=a+2
#Döngü sonu
print ("Toplam=",Top)
