'''
Örnek 7.7.
7 ile 77 arasında 7 adet rastgele tamsayı üreten ekranda gösteren programı yazınız.
@author:Bülent Çobanoğlu
'''
import random
for i in range (7):
    print (random.randint(7,77),end=' ')
