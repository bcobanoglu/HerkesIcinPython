'''
Örnek 17.8. Bir programın kaç adımda bittiği (yürütme/çalışma süresini)
monotonic saat kullanarak ölçen basit bir program yazınız
@author:Bülent Çobanoğlu
'''
import time
t0 = time.monotonic() #sayacı tut
#çalışma süresi hesaplanacak fonksiyon
time.sleep(0.5) #0.5 saniye bekle
t1 = time.monotonic() #sayacı bırak
print('Başla : {:.2f}'.format(t0))
print('Bitir : {:.2f}'.format(t1))
print('Süre  : {:.2f}'.format(t1-t0))
