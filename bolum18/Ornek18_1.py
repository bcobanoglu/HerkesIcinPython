'''
Örnek 18.1. Verilen bir listenin her bir elemanının sayı olup/olmadığını test eden basit bir assert uygulamasını gerçekleştiren programı yazınız.
@author:Bülent Çobanoğlu
'''
def test_karakter(liste):
    for i in liste:
        try:
            #i: bir sayı mı?
            assert str(i).isnumeric()
        #sayı değilse except bloğu çalışır
        except AssertionError:
            print("{} sayı değil.".format(i))
#Ana program
liste = [1, 2, 3, 'c', 4, 5, "a"]
test_karakter(liste)
