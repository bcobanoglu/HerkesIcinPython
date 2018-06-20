#author:bulend hoca
#Örnek 10.9.Kuyruğa eleman ekleme / çıkarma işlemleri
from collections import deque
# -*- coding: UTF-8 -*-
kyrk = deque(["Erik", "Can", "Meryem"])
kyrk.append("Tuna")  #Tuna kuyrukta
kyrk.append("Gizem") #Gizem kuyrukta
kyrk.popleft()  #Erik(baştaki) ayrıldı
kyrk.popleft()  #Can ayrıldı
print (list(kyrk)) #listeye dönüştürüldü
