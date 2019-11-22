"""Herkes için Python kitabı, Yazar:Bülent Çobanoğlu
Örnek 20.3.  
Bir 4*4 birim matrisi oluşturup ekranda gösteren
ve bu matrisin izini hesaplayan program
"""
import numpy as np
d = np.eye(4, dtype=int)
print (d) 
print ("Matrisin izi:")
print (np.trace(d))
