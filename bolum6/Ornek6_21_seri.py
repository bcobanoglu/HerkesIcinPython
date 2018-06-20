'''
Örnek 6.21.
s=1+1/2+1/3+1/4+……… +1/n şeklinde verilen serinin toplamını bulunuz.
@author: Bülent Çobanoğlu
'''
ST=0
n=int(input('Terim sayisi.:'))
for x in range (1,n+1):
    ST=ST+1/x
print("Toplam=",ST)
