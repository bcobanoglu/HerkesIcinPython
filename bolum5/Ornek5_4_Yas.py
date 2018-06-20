'''
@author:Bülent Çobanoğlu
Örnek 5.4. Girilen yaş değerine göre kişinin içinde bulunduğu yaşam evresini verilen tabloya göre ekranda gösteren programı kodlayınız. Girilen değerlere göre istenen program çıktısı:
Yaşınız..:	İstenen Çıktı
0… 2	Bebeklik
3… 13	Çocukluk
14… 21	Ergenlik
22… 63	Yetişkinlik
64+ ise	Yaşlılık
'''
# -*- coding: UTF-8 -*-
yas=int(input('Yaşınız..:'))
if yas <= 2:
    print ("Bebeklik")
elif yas <= 13:
    print ("Çocukluk")
elif yas <= 21:
    print ("Ergenlik")
elif yas <= 63:
    print("Yetişkinlik")
else:
    print ("Yaşlılık")
