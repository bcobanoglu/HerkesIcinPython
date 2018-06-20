'''
Örnek 18.5. “HesapMakinesi.py” isimli 4 işlem yapan bir program üzerinde birim testi yapacak bir programı yazınız.
@author:Bülent Çobanoğlu
'''
import unittest #birim test modülü
import HesapMakinesi #test edilecek program

class test_DortIslem(unittest.TestCase):
    def test_topla(self): #(2+3)==5 mi?
        self.assertEqual(HesapMakinesi.topla(2, 3), 5)
        print("\n Fonk: test_topla() ")
    def test_carp(self): #(2*3)==6 mı?
        self.assertEqual(HesapMakinesi.carp(2, 3), 6)
        print("\n Fonk:test_carp() ")
    def test_cikar(self): #(6-3)==3 mi?
        self.assertEqual(HesapMakinesi.cikar(6, 3),3)
        print("\n Fonk:test_cikar() ")
    def test_bol(self): #(6/3)==2 mi?
        self.assertEqual(HesapMakinesi.bol(6, 3), 2)
        print("\n Fonk:test_bol() ")

#Ana program
if __name__ == '__main__':
    unittest.main()
