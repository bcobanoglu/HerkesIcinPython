'''
Örnek 5.2.  Birbirinden farklı üç sayı içerisinden en büyüğünü bulan programı kodlayınız.
@author: Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
print ("Gir, üç sayı")
s1=int(input('s1..:'))
s2=int(input('s2..:'))
s3=int(input('s3..:'))
Enb=s1
if s2 > Enb:
    Enb = s2
if s3 > Enb:
    Enb = s3
print("En büyüğü.:",Enb)
