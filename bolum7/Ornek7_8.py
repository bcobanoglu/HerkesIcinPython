# sayı tahmin oyunu
#@author:Bülent Çobanoğlu
# -*- coding: UTF-8 -*- 
import random
def tahmin(a):
    sayac,puan=0,100
    print("İlk Tahmininiz..:");
    while True:
        tahmin =int(input())
        sayac+=1
        if tahmin == a:
            print("Bravo!",sayac,".de",a,"i bildiniz")
            break
        elif tahmin < a:
             print("Daha büyük bir sayı gir!")
        else:
            print("Daha küçük bir sayı gir!")
        puan-=10
    print("Puanınız..:",puan)
#Ana program
tut = random.randint(1,100)
tahmin(tut)
