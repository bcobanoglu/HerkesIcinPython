'''
Örnek 7.4.
1’den 10’a kadar ki sayıların karesini alan programı map fonksiyonunu kullanarak kodlayınız.
@author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
def kare(a):
    return a**2
sayi = range(1,10)#1-9 arası sayılar
map_cikti = map(kare, sayi)
#print(map_cikti):object hatası
print(list(map_cikti))
#listeye dönüştürüp yazdırdık
