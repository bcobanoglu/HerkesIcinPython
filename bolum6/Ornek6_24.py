'''
Örnek 6.24.
s=1+1/2!+1/3!+1/4!+……… +1/n! şeklinde verilen serinin toplamını bulunuz.
@author: Bülent Çobanoğlu
'''

ST=0
f=1
n=int(input('Terim sayisi.:'))
for x in range (1,n+1):
    f=f*x
    ST=ST+(1/f)
print("Toplam=",ST)
