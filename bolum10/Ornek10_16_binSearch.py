#author-bulend hoca
#ikili arama fonksiyonu
def binArama(Alist, aranan):
    alt = 0; ust = len(Alist)-1
    bayrak = False
    while alt<=ust and not bayrak:
        orta = (alt + ust)//2
        if Alist[orta] == aranan:
            bayrak = True
        elif aranan < Alist[orta]:
            ust = orta-1
        else:
            alt = orta+1
    return bayrak
#çift sayılar listesi
A= [i for i in range(60) if i % 2 == 0]
ara=int(input('Aranan..:'))
if binArama(A, ara)==True:
    print("Sirasi:",A.index(ara)+1)
else:    print('Listede yok')
