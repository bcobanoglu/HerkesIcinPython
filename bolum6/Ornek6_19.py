'''
Örnek 6.19. İlk 100 sayı içerisindeki asal sayıları ve bu sayıların adedini ekrana yazan programı kodlayınız.
@author: Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
N=100
asal=5 #ilk 5 asal sayıyı biliyoruz
print ("1 2 3 5 7 ")
for i in range (7, N+1, +2):
    if (i%3!=0 and i%5!=0 and i%7!=0):
        asal=asal+1
        print (i, end=' ')
print("\nAsal sayi adedi:", asal)
