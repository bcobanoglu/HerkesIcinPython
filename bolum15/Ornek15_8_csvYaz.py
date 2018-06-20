#author:Bülent Çobanoğlu
#csv modülünü import et
import csv
#yeni olaylar dizisi
yeniOlay=[["22/08/2018, 8:00, Bayramlaşma , info@teknecik.org.tr, 212 4521537, Teknecik köyü derneği-İstanbul"],
          ["25/07/2018, 8:00, Tatil , tatil@teknecik.org.tr, 446 34556767, Teknecik köyü-Erzincan"]        ]
#'OnemliOlaylar.csv' dosyasını ekleme amaçlı aç
with open('OnemliOlaylar.csv', 'a', newline='') as f:
    ekleDosya = csv.writer(f) #ekleDosya isimli writer nesnesi tanımlandı
    ekleDosya.writerows(yeniOlay) #ekleDosya'ya yeni olaylar yazıldı
