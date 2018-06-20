'''
Örnek 10.3.
Girilen para miktarını şu anda kullanılmakta olan para kupürlerine
‘200 - 100 - 50 – 20 -10 – 5 – 1 – 0.5’ göre en az sayıda kupür ile ödemek için bir veznedara yardımcı olacak programı yazınız.
#author-bulend hoca
'''
# -*- coding: UTF-8 -*-
kupur=[200,100,50,20,10,5,1,0.5]
para=float(input('Para miktarı..:'))
for i in range(8):
    sayi=float(para)//kupur[i]
    if sayi !=0:
        print(sayi,"adet",kupur[i])
    para=para-sayi*kupur[i]
