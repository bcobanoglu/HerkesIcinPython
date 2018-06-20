#Menü fonksiyonu
def menuSecim():
    print('[1]. Listele')
    print('[2]. Ekle')
    print('[3]. Sil')
    print('[4]. Ara')
    print('[5]. Çıkış')
    menuSec = 0
    while menuSec != 5:
        menuSec = int(input("Seçiminiz: "))
        if menuSec == 1:
            listele()
        elif menuSec == 2:
            ekle()    
        elif menuSec == 3:
            sil()
        elif menuSec == 4:
            ara()
        elif menuSec == 5:
            cikis()    
        else:
            print("1-5 arasında seçim yapınız!!")
    
numaralar = {}#Kayıtları tutan liste
   
#Dosyadaki tüm kayıtları okuyan fonksiyon
def dosyadanOku():
    f = open('rehber.txt', 'r')
    for x in f.readlines():
        ad, tlfn = x.strip().split()
        numaralar[ad] = tlfn
        f.close()
#Rehberdeki tüm kayıtları listeleyen fonksiyon
def listele():        
    #kayıtları yükle
    dosyadanOku()
    #Tüm kayıtları ekrana yaz
    print("Telefon Rehberim:")
    for x in numaralar.keys():
        print("Ad-Soyad: ", x, "\tNumara:", numaralar[x])
        print()
#Rehbere yeni kayıt ekleyen fonksiyon        
def ekle():    
    print("Ad-Soyad ve Numara Ekle")
    ad = input("Ad-Soyad: ")
    tlfn = input("Numara: ")
    #numaralar[ad] = tlfn
    kayit= ad + '\t' + tlfn + '\n'
    #kayıdı dosyaya yaz
    f = open('rehber.txt', 'a')
    f.write(kayit)
    f.close()
#Rehberden bir kayıdı silen fonksiyon
def sil():
    dosyadanOku()
    silAd = input("Silinecek ad: ")
    if silAd in numaralar.keys():
        del numaralar[silAd]
        f = open("rehber.txt", 'w')
        for ad, tlfn in numaralar.items():
            kayit = ad + '\t' + tlfn + '\n'
            f.write(kayit)
            f.close()
            print("Başarı ile silindi")
    else:
        print("Kayıt bulunamadı")
#Rehberdeki bir kaydı arayan fonksiyon
def ara():
    dosyadanOku()
    ad = input("Aradığınız isim: ")
    if ad in numaralar:
        print("Numarası", numaralar[ad])
    else:
        print(ad, "bulunamadı")
#Çıkış fonksiyonu
def cikis():
    print("Program sonlandırıldı")
    raise SystemExit()
#Ana program    
if __name__ == "__main__":
    menuSecim()