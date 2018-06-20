'''
Örnek 6.7. Dört işlem (toplama, çıkarma, çarpma ve bölme) yapan hesap makinesi uygulamasını kullanıcının devam etmek isteyip/istememesine göre kodlayınız.
@author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
while True:
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
    cvp=input("Devam etmek istiyormusunuz(e/h)?")
    if cvp=='h':
        break
    else:
        continue
print("Hesap makinesi kapandi")
