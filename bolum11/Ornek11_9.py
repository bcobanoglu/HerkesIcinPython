#author:Bülent Çobanoğlu
#Üst sınıf
class Hayvan:
    def __init__(self,ad):
       self.ad=ad

#Türetilmiş alt sınıflar
class Inek(Hayvan):
    def Konus(self):
         return 'Möö'

class Kedi(Hayvan):
    def Konus(self):
         return 'Miyav'

class Kopek(Hayvan):
    def Konus(self):
         return 'Hav Hav'

#Ana Program
a=[Inek('İnek'),
   Kedi('Kedi'),
   Kopek('Köpek')]
for i in a:
    print (i.ad+':'+i.Konus())
