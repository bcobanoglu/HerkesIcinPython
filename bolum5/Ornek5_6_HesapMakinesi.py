'''
Örnek 5.6. Dört işlem (toplama, çıkarma, çarpma ve bölme) yapan bir hesap makinesi programını kodlayunız.
{ Sayı girişi ve işlem operatörü klavyeden girilecek }.
@author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
s1=int(input('s1..:'))
s2=int(input('s2..:'))
op =input('islem..:')
if (op=='+'):
    S=s1+s2
elif (op=='-'):
    S=s1-s2
elif (op=='*'):
    S=s1*s2
elif (op=='/'):
    S=s1/s2
else:
    print("Hatalı seçim")

print("Sonuc=",S)
