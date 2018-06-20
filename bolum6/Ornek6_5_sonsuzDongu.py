'''
Örnek 6.5. Girilen sayı sıfırdan farklı olduğu sürece o sayının karesini alan programı yazınız.
@author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
print("Cikis icin 0 giriniz\n")
while True:
    A=int(input('Gir bir sayi.:'))
    print("karesi= ", A*A);
    if (A==0):
        break
#Döngü sonu
