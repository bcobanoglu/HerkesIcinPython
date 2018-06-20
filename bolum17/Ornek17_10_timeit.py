'''
Örnek 17.10.
10 elemanlı bir listede doğrusal arama yapan algoritmanın { veya dogrusalArama() fonksiyonunun }
performansını timeit ile hesaplayan bir program yazınız.
@author:Bülent Çobanoğlu
'''
liste = [1987, 8765, 10982, 1875, 1452, 5634, 29765, 12534, 88768, 90012]
def test(sayi): #doğrusal arama algoritması
    for i in range (0,100000):
        if sayi in liste:
            bulundu = True

import timeit
sayi=1453
print("Çalışma süresi:")
print(timeit.timeit("test(sayi)", setup="from __main__ import test, sayi", number=1))
