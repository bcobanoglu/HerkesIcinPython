'''
Örnek 11.1.
Bir araba sınıfından ‘Kamyon’, ‘Taksi’ nesnelerini oluşturup,
bazı özelliklerini ekrana yazdıran uygulama
@author: Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
class Araba():
    # Sınıf özellikleri
    model="BMC"
    renk ="Kırmızı"
    kapasite = 26000
    silindir = 6

kamyon=Araba() #Kamyon nesnesi
taksi=Araba() #Taksi nesnesi
#Taksi nesnesinin bazı özellikleri değiştirildi
taksi.model="Renault Scenic"
taksi.silindir=4
print("Kamyon modeli..:",kamyon.model)
print("Taksi modeli..:",taksi.model)
