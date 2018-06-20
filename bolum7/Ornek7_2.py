#cevir fonksiyonu
def cevir(f):
    return ((f - 32) / 1.8)
#Ana program
f=float(input('Fahrenhayt degeri:'))
C = cevir(f);
print(C , " derecedir")
