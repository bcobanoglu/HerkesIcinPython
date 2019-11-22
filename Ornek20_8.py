"""Herkes için Python kitabı
Çift sayıları 0 ile değiştirme
"""
import numpy as np
d = np.random.randint(0,100,24) #dizi
print (d) # dizi elemanları ekrana yazdırıldı
tek = np.where(d % 2 != 0, d, 0)
# dizideki çift sayılar ‘0’ yapıldı
print ("=============\n", tek)
