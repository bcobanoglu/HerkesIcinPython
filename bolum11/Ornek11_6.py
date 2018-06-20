#author:Bulend Hoca
class Araba():
    #yapıcı metot ve parametreleri
    def __init__(self, hiz, renk, durum):
        self.hiz=hiz
        self.renk=renk
        self.durum=durum

    #özel str() metodu
    def __str__(self):
        return "Hız: {}\nRenk: {}\nDurum: {}".format(self.hiz,self.renk,self.durum)
    def calis(self):
        print ("Çalışıyor...")
    def dur(self):
       print("Duruyor...")

#Araba sınıfından kalıtımla Kamyon sınıfını türet
class Kamyon(Araba):
    def __init__(self, hiz, renk, durum):
        Araba.__init__(self, hiz,renk,durum)
#Araba sınıfından kalıtımla Taksi sınıfını türet
class Taksi(Araba):
    def __init__(self, hiz,renk,durum, km):
        Araba.__init__(self, hiz,renk,durum)
        self.km=km
    def __str__(self):
        return Araba.__str__(self)+"\nKm..:"+str(self.km)
#Test fonksiyonu
def test():
    k=Kamyon(70,"kırmızı",False)
    print (k)
    k.dur()
    print("---------------------")
    t=Taksi(90,"sarı",True, 54000)
    print (t)
    t.calis()

if __name__=="__main__":
    test()
