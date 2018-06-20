#0-N arasında 3 bölünenlerin ortalaması
# -*- coding: UTF-8 -*-
Sayac=0
T=0
N=int(input("Gir bir sayi..:"))
X=N-(N % 3) 
while X>0:
    T=T+X
    X=X-3
    Sayac=Sayac+1
#Döngü sonu
Ort=T/Sayac
print ("Ortalama =", Ort)
