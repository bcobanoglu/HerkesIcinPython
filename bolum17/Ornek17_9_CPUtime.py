'''
Örnek 17.9. 10 elemanlı bir listede doğrusal arama yapan algoritmanın { veya dogrusalArama() fonksiyonunun }
 performansını CPU çalışma süresi üzerinden hesaplayan bir program yazınız.
@author:Bülent Çobanoğlu
'''
import time
liste = [1987, 8765, 10982, 1875, 1452, 5634, 29765, 12534, 88768, 90012]
def dogrusalArama(sayi): #doğrusal arama algoritması
    for i in range (0,100000):
        if sayi in liste:
            bulundu = True
#Ana program
t0 = time.process_time()
dogrusalArama(1453)
t1 = time.process_time()
print ('CPU Çalışma Süresi:', (t1-t0),'sn')
