#author- Bulend Hoca
# -*- coding: UTF-8 -*-
Fal = {1:'Seviyor',2:'Sevmiyor',3:'Seviyor', 4:'Sevmiyor',5:'Seviyor',
       6:'Sevmiyor',7:'Seviyor', 8:'Sevmiyor',9:'Seviyor', 10:'Sevmiyor',
     }
for i in range(1,len(Fal)):
    Fal.popitem()#del Fal[i]
    print (Fal)