'''
Örnek 8.11. Şifre/password sorgulaması yapan uygulama:
Basit bir şifre/password sorgulaması yapan programı yazınız.
@:author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
sayac=0
while True:
    sifre=input("password giriniz..:")
    if "elma"==sifre:
        print ("sifre dogru")
        break
    sayac+=1
    if sayac>=3:
        print ("hakkiniz doldu")
        break
