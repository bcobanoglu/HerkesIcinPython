#author:Bulend Hoca
class Anne():
    #yapıcı metot ve parametreleri
    def __init__(self, Amal):
        self.Amal=Amal

    def __str__(self):
        return "Anneden:" + self.Amal
class Baba():
    #yapıcı metot ve parametreleri
    def __init__(self, Bmal):
        self.Bmal=Bmal

    def __str__(self):
        return "Babadan:" + self.Bmal

#Anne ve Baba sınıfından çoklu kalıtımla Evlat sınıfı
class Evlat(Anne, Baba):
    def __init__(self, Amal, Bmal, kendiM):
        #Anne ve Baba sınıfından örnekler oluşturuldu
        Anne.__init__(self, Amal)
        Baba.__init__(self, Bmal)
        self.kendiM=kendiM
    def __str__(self):
        return Anne.__str__(self)+"\n"+Baba.__str__(self)\
               +"\nAlın terim:"+str(self.kendiM)
#Test fonksiyonu
def test():
    print("----Mirasım-----")
    miras=Evlat("Zeytinlik","Villa","BMW")
    print (miras)
if __name__=="__main__":
    test()
