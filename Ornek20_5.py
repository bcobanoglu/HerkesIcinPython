"""Herkes için Python kitabı, Yazar: Bülent Çobanoğlu
Program adı: 1D den 2D ye dönüşüm
"""
import numpy as np
#Tek boyutlu d dizisi (1-12)
d = np.arange (1, 13)
# d dizisinden 3*4 lük A matrisi elde edildi.
A = d.reshape(3,4) 
print (A)
