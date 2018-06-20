#author:Bülent Çobanoğlu
#csv modülünü import et
import csv
#f ile temsil edilen 'OnemliOlaylar.csv' dosyasını aç
with open('OnemliOlaylar.csv', 'r', newline='\n') as f:
    #dosyadaki ',' ile ayrılmış her bir veriyi okuDosya
    #değişkeninde tut
    okuDosya = csv.reader(f, delimiter=',')
    #okuDosya'daki her bir veriyi ekrana yaz
    for satir in okuDosya:
       print(', '.join(satir))
