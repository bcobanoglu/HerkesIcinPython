#tuple veri yapısındaki en son elemanın değerini ‘Swift’ olarak değiştiren program
#Bülent Çobanoğlu
dil=('C', 'C++', 'C#', 'Java', 'Python', 'ObjeC')
dil=list(dil) #listeye donustu
dil.remove('ObjeC') #ObjeC silindi
dil.append('Swift') #Swift eklendi
print(tuple(dil))
