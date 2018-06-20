'''
Örnek 6.23 .
s=1+1/2+1/4+1/8+……… +1/2^n şeklinde verilen serinin toplamını bulunuz.
@author: Bülent Çobanoğlu
'''
ST=1
Payda=1
n=int(input('Terim sayisi:'))
for x in range (2,n+1):
    Payda=Payda*2
    ST=ST+1/Payda
print("Toplam=",ST)
