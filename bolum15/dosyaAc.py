metin = '''Ben bir ağacım, içten kökten gülerim,
Aşk çeşmesi döndükçe sevincim de döner.
Mevlana'''
#dosya yazma amaçlı açıldı
f1 = open('mevla.txt', 'w')
f1.write(metin) #dosyaya veriler yazıldı
f1.close() #1.dosya kapatıldı

#şimdi dosyayı açıp, okuyalım.
f2 = open('mevla.txt',"r")
while True:
    sat = f2.readline() #okunanı sat değişkeninde tut.
    #eğer satır sonu ise döngüden çık
    if len(sat) == 0: 
        break
    print (sat,) #sat içeriğini ekrana yaz
f2.close() #2.dosya kapatıldı