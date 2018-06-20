'''
Örnek 18.4. 7.bölümde fonksiyonunu verdiğimiz (Örnek 7.6.) Fizz Buzz Oyunu için bir test programı yazınız.
@author:Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
import unittest
#Test edilecek fonksiyon:fizzBuzz
def fizzBuzz(sayi):
    x=int(sayi) #sayı string ise int'e dönüştür
    if x % 15 == 0:
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    else:
        return x
#Testi yapan TestCase sınıfımız: testFizzBuzz
class testFizzBuzz(unittest.TestCase):
    #normal sayıların testi
    def test_normalSayilar(self):
       #assertEqual alternetifi:assertIs
        self.assertIs(fizzBuzz(1), 1)
        self.assertEqual(fizzBuzz(4), 4)
        self.assertEqual(fizzBuzz(7), 7)
    #"Fizz" sayıların testi
    def test_fizzSayilar(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")
    #"Buzz" sayıların testi
    def test_buzzSayilar(self):
        self.assertEqual(fizzBuzz(5), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(50), "Buzz")
    #"FizzBuzz" sayıların testi
    def test_fizzbuzzSayilar(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
    #string girilen sayıların testi
    def test_stringSayilar(self):
        snc = fizzBuzz("3")
        self.assertEqual(snc, "Fizz")
        snc = fizzBuzz("5")
        self.assertEqual(snc, "Buzz")
        snc = fizzBuzz("15")
        self.assertEqual(snc, "FizzBuzz")
#Test ana(main) metodu çağrılıyor
if __name__ == '__main__':
    unittest.main()
