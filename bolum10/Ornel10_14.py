# -*- coding: UTF-8 -*-
#author:bulend hoca
gunler= ('','Pazartesi', 'Salı', 'Carsamba', \
         'Persembe','Cuma', 'Cumartesi', 'Pazar')
# enumerate() ile indis ve değerini aldık 
for i, deger in enumerate(gunler):
    print(str(i) + ".." + deger)
