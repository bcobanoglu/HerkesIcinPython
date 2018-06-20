#@author:Bülent Çobanoğlu
# -*- coding: UTF-8 -*- 
def Tek(s1,s2):
    sayac=0
    if s1%2 !=0:#s1:tek ise yazdir
        for i in range(s1,s2+1,+2):
            print (i,end=' ')
            sayac+=1 #sayac 1 artir
    else:#s1:cift ise tek'e donustur yazdir
        for i in range(s1+1,s2+1,+2):
            print (i,end=' ')
            sayac+=1 #sayac 1 artir
    return sayac
#Ana program
import random
a=random.randint(1,100)
b=random.randint(1,100)
print("s1=",a,"\ns2=",b)
if a>b:
    a,b=b,a #iki degiskeni yerdegistir
print ("\nAdedi.:",Tek(a,b))
