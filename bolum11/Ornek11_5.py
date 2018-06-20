class Personel:
    def __init__(self, ad, soyad):
        self.ad=ad
        self.soyad=soyad
    @property
    def mail(self):
        return '{}{}@gmail.com'\
          .format(self.soyad,self.ad)
    @property
    def Ad(self):
        return '{} {}'\
          .format(self.ad,self.soyad)
    @Ad.setter
    def Ad(self, isim):
        ad, soyad=isim.split(' ')
        self.ad=ad
        self.soyad=soyad

kisi1=Personel('bulent','cobanoglu')
kisi1.Ad='bayram aksu'
print("Ad:",kisi1.ad)
print("Soyad:",kisi1.soyad)
print("mail:",kisi1.mail)
