'''
Örnek 11.3.
Bir sınıfın nasıl tanımlanacağını, bu sınıftan nasıl nesneler türetileceğini
ve türetilen bu nesnelere nasıl çağrı yapılacağını bir araba örneği ile açıklayınız.
@author:Bülent
'''
class Araba():
    #yapıcı metot ve parametreleri
    def __init__(self, model,renk,motor,kapasite):
        self.model=model
        self.renk=renk
        self.motor=motor
        self.kapasite=kapasite
    #özel str() metodu
    def __str__(self):
        return "Model: {}\nRenk: {}\nMotor: {}\nKapasite: {}".format(self.model,self.renk,self.motor,self.kapasite)
#Ana program
#Araba sınıfından nesneler türet ve ekrana yaz
kamyon=Araba("BMC","Kırmızı", 3000, 9000 )
print (kamyon)
print("---------------------")
taksi=Araba("Renault", "Füme", 1600, 2800)
print (taksi)
