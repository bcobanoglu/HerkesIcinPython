#author:bulend hoca
A=(2, 3, 5, 8, 9, 12, 34, 6, 77)
Ara=int(input("Aranan Sayi: "))
if Ara in A:#True ise
    i=A.index(Ara)#Arananin indisi
    print("Aranan", i+1, ". sirada bulundu")
else:#False ise
    print ("Aranan bulunamadi.")
