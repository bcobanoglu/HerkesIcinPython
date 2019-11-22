"""
Kitap: Herkes için Python
Yazar: B.Çobanoğlu
Program: Matris elemanlarını sıralama
"""
import numpy as np
a = np.array ([[3,5,9], [4,6,1], [7,8,2]])
aS = np.sort(a, axis = None)
for i in aS.flat:
    print (i)
