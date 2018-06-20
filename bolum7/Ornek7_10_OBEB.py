#@author:Bülent Çobanoğlu
# -*- coding: UTF-8 -*- 
def obeb(m,n):
    while m%n != 0:
        eskiM = m
        eskiN = n

        m = eskiN
        n = eskiM % eskiN
    return n
#ana program
import random
m=random.randint(1,100)
n=random.randint(1,100)
print('OBEB({},{})={}'.format(m,n,obeb(m,n)))
