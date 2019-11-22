"""Herkes için Python kitabı
Transpoze
"""
import numpy as np
A=[
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 0, 4],
  ]
#Önce liste diziye dönüştürülür
d = np.array(A)
B = d.T #A nin transpozesi
print("Transpozesi:\n",B)

