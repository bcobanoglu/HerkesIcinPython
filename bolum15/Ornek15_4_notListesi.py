#author:Bülent Çobanoğlu
notlar= ["Ömer Can :90", "Berat Can :95",
         "Levent Çoban :100", "Bade Zehra :50",
         "Ekrem Can :68" ]
#dosya yazma amaçlı açıldı
f1 = open('notlar.txt', 'w')
for n in notlar:
    f1.write(n+"\n") #notlar alt alta yazıldı
f1.close() #1.dosya kapatıldı

#şimdi dosyayı açıp, okuyalım.
print ("Ad-Soyad  :Notu")
print ("################")
f2 = open('notlar.txt',"r")
while True:
    liste = f2.read() #okunanı liste'de tut.
    #eğer liste sonu ise döngüden çık
    if len(liste) == 0:
        break
    print (liste,) #liste içeriğini ekrana ya
f2.close() #2.dosya kapatıldı
