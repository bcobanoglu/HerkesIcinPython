'''
Örnek 17.1. Kullandığınız bilgisayarın  (daha doğrusu işletim sisteminin)
hangi tarihi ‘zamanın başlangıcı-epoch’ olarak kabul ettiğini gösteren bir program yazınız.
@author:Bülent Çobanoğlu
'''
import time #time modülünü çağır
#Tarihin sıfır/başlangıç(0) noktasını al
epok=time.gmtime(0)
#başlangıç tarihini struct_time veri tipinde yaz.
print(epok)
#Tarihi gün / ay / yıl formatında yaz
print (epok.tm_mday,'/',epok.tm_mon,'/',epok.tm_year)
print ("Epoch tarihinden bugüne geçen süre:", time.time(), "sn")
