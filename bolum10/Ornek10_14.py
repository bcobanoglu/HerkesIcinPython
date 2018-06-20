'''
haftanın günlerinin rakamsal karşılığını veren programı tuple veri yapısını kullanarak kodlayınız
'''
# -*- coding: UTF-8 -*-
gunler= ('','Pazartesi', 'Salı', 'Carsamba', \
         'Persembe','Cuma', 'Cumartesi', 'Pazar')
# enumerate() ile indis ve değerini aldık
for i, deger in enumerate(gunler):
    print(str(i) + ".." + deger)
