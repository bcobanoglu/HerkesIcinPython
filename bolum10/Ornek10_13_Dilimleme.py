#author:bulend hoca
# -*- coding: UTF-8 -*-
#Dilimleme Örneği:
#tuple veri yapısındaki en son elemanın değerini ‘Swift’ olarak değiştiren program

dil=('C', 'C++', 'C#', 'Java', 'Python', 'ObjeC')
#dil[5]='Swift'#Gecersiz atama
yeniDil=(dil[:5], 'swift')
print(yeniDil)
