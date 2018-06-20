#varolan dosya 'a'-append modunda açıldı
f = open('mevla.txt', 'a')
#dosyaya yeni veriler yazılıyor
f.write("\nBuğdayın samandan ayrılması gibi\n") 
f.write("iyiyle kötüyü ayırmak gerekir.")
f.close() #1.dosya kapatıldı

#şimdi dosyayı açıp, okuyalım.
f2 = open('mevla.txt',"r")
while True:
    sat = f2.readline() #okunanı sat’da tut.
    #eğer satır sonu ise döngüden çık
    if len(sat) == 0: 
        break
    print (sat,) #sat içeriğini ekrana yaz
f2.close() #2.dosya kapatıldı
