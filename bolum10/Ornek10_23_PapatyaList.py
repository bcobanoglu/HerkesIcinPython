# -*- coding: UTF-8 -*-
#author:Bülent Çobanoğlu
# Papatya Falı
import random
Fal = ['Seviyor','Sevmiyor','Seviyor', 'Sevmiyor','Seviyor',
       'Sevmiyor','Seviyor', 'Sevmiyor','Seviyor', 'Sevmiyor',
     'Seviyor', 'Sevmiyor','Seviyor','Sevmiyor','Seviyor',
     'Sevmiyor','Seviyor', 'Sevmiyor','Seviyor']
for i in range(0,18):
    x=random.randint(0,1)#Seviyor yada Sevmiyoru seç
    Fal.pop(x)
    print (Fal)
