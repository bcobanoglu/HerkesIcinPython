'''
Örnek 6.11. Girilen iki pozitif tamsayının çarpımını, çarpma operatörü kullanılmadan hesaplayan programı for döngüsü ile kodlayınız.
@author: Bülent Çobanoğlu
'''
carp = 0 #Gerçekte toplama değişkeni
s1=int(input('Sayi1.:'))
s2=int(input('Sayi2.:'))
for x in range (s1):
    carp = carp + s2
#Dongu sonu
print(s1,'*', s2,'=',carp)
