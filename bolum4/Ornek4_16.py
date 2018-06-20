'''
Örnek 4.16. Üç kenar uzunluğu verilen bir üçgenin alanını hesaplayan programı kodlayınız.
@author: bülent cobanoglu
'''
a=int(input('a kenarı..:'))
b=int(input('b kenarı..:'))
c=int(input('c kenarı..:'))
#üçgenin yarı çevresi
u=(a+b+c)/2
#alanı hesapla
alan=(u*(u-a)*(u-b)*(u-c))**0.5
print('Alan=',alan)
