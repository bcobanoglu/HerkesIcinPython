#author:Bülent Çobanoğlu
import unittest

class testStringMetotlar(unittest.TestCase):

    def test_BuyukMu(self):
        self.assertTrue('BADE'.isupper())
        self.assertFalse('Bade'.isupper())

    def test_kucukBuyukHarfDegistir(self):
        self.assertEqual('HanzaR'.swapcase(), 'hANZAr')

    def test_Ara(self):
        self.assertIn('z','hanzar', 'hanzar içinde z varmı?')
        self.assertRegex('hanzar', r'^h', 'metin h ile mi başlıyor?')

    def test_elemanSayilari(self):
        a= 'Hanzar'
        b= 'hanzar'
        self.assertCountEqual(a, b, 'elemnalar birebir aynı mı?')

    def test_split(self):
        s = 'Gunhan Bayrak'
        self.assertEqual(s.split(), ['Gunhan', 'Bayrak'])
        #s içerisinde ayraç karakteri veya boşluk karakteri yoksa hata üret
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
