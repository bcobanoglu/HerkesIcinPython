'''
Örnek 6.25.  s=x+x2+x3+x4+……… +xn şeklinde verilen serinin toplamını bulunuz.
@author: Bülent Çobanoğlu 
'''
ST=0
x=int(input('x.:'))
n=int(input('Terim sayisi.:'))
for us in range (1,n+1):
    ST=ST+x**us
print("Toplam=",ST)
