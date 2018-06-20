#Birim test şablonu
#author:Bülent Çobanoğlu
import unittest

class Testim(unittest.TestCase):
    def test_buyukEsitmi(self):
        self.assertGreaterEqual(3, 4)

if __name__ == '__main__':
    unittest.main()
