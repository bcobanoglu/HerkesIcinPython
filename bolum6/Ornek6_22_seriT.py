'''
Örnek 6.22.
s=1-1/2+1/3-1/4+1/5-……… ±1/n şeklinde verilen serinin toplamını bulunuz.
@author: Bülent Çobanoğlu
'''
ST=0
sgn=+1
n=int(input('Terim sayisi.:'))
for x in range (1,n+1):
    ST=ST+(1/x)*sgn
    sgn=-sgn
print("Toplam=",ST)
