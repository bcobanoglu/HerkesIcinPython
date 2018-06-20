'''
Örnek 15.6. Menülü Telefon Rehberi Uygulaması
@author:Bülent Çobanoğlu
'''
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

numaralar = {} #Kayıtları tutan liste
#Rehberdeki tüm kayıtları listeleyen fonksiyon
def listele():
    #kayıtları ekrana yaz
    print("Telefon Rehberim:")
    for x in numaralar.keys():
        print("Ad-Soyad: ", x, "\tNumara:", numaralar[x])
        print()
#Listeye yeni kayıt ekleyen fonksiyon
def ekle():
    print("Ad-Soyad ve Numara Ekle")
    ad = input("Ad-Soyad: ")
    tlfn = input("Numara: ")
    numaralar[ad] = tlfn
#Listeden bir kayıdı silen fonksiyon
def sil():
    ad = input("Rehberden silinecek kayıt: ")
    if ad in numaralar:
        del numaralar[ad]
        print("başarı ile silindi")
    else:
        print(ad, "bulunamadı")
#Lesteden bir kaydı arayan fonksiyon
def ara():
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
