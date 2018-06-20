#author:Bulend Hoca
class TV:
    #setter fonksiyonları
    def setUz(self, u):
        self.__boy = u
    def setEn(self, e):
        self.__en = e

    #getter fonksiyonu
    def getSes(self):
        return self.__boy*self.__en

#Ana Program
nesne=TV()
frkns=nesne.setUz(10.0)
gnlk=nesne.setEn(8.0)
print("Ses Ayarı: ", nesne.getSes())
print("Erişim: ", dir(nesne))
