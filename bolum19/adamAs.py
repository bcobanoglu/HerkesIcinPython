'''
Örnek 19.1. Adam Asmaca Oyunu
'''
import random
ADAM = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |'
]
print ("Programlama dillerini tahmin et")
progDiller = ['ADA', 'COBOL', 'BASIC', 'FORTRAN', 'PYTHON', 'GO',
              'RUBY', 'JAVA', 'SWIFT', 'LISP', 'MATLAB', 'CSHARP']

class AdamAsmaca():
    #AdamAsmaca oyunu metotları
    def __init__(self, tahmin):
        self.hataliGirisler = 0
        self.tahmin = tahmin
        self.oyun_ilerlet = list('_' * len(self.tahmin))

    def indisBul(self, harf):
        #Bu metot bir harfi alır ve onun kelimedeki yerini/indisini bulur
        return [i for i, char in enumerate(self.tahmin) if harf == char]

    def hatali_harf(self, girilen):
        #Bu metot girilen karakterin hatalı olup olmadığını kontrol eder
        return girilen.isdigit() or (girilen.isalpha() and len(girilen) > 1)

    def yaz_OyunDurumunu(self):
        #Bu metot kalan boşlukları hesaplar
        print('\n')
        print('\n'.join(ADAM[:self.hataliGirisler]))
        print('\n')
        print(' '.join(self.oyun_ilerlet))

    def guncelleOyunu(self, harf, indis):
        for i in indis:
            self.oyun_ilerlet[i] = harf

    def harfAl(self):
        grlnHarf = input('\nLütfen bir harf gir: ')
        return grlnHarf.upper()

    def Oyun(self):
        while self.hataliGirisler < len(ADAM):
            self.yaz_OyunDurumunu()
            grlnHarf = self.harfAl()

            # Girilen harfin geçerliliğini test et
            if self.hatali_harf(grlnHarf):
                print('Bir harf gir!')
                continue
            # Eğer harf daha önce girilmişse
            if grlnHarf in self.oyun_ilerlet:
                print('Bu harfi söylemiştin')
                continue
            # Eğer girilen harf varsa
            if grlnHarf in self.tahmin:
                indis = self.indisBul(grlnHarf)
                self.guncelleOyunu(grlnHarf, indis)
                # Eğer harfler tamamlandı ise
                if self.oyun_ilerlet.count('_') == 0:
                    print('\nBravo Kazandın!')
                    print('Kelime: {0}'.format(self.tahmin))
                    quit()
            else:
                self.hataliGirisler += 1
        print("\nOoo! Kaybettin!")

if __name__ == '__main__':
    tahmin = random.choice(progDiller)
    adamAs = AdamAsmaca(tahmin)
    adamAs.Oyun()
