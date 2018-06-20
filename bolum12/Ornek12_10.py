'''
Örnek 12.10.  kullanıcı tanımlı istisna örneği: myHatam
@author:Bülent Çobanoğlu
'''
class myHatam(Exception):
    #Bu modüldeki tum hataların ana sınıfı
    ad = "benimHatam.py"
class ilkHatam(myHatam):
    #myHatam sınıfından türetilen alt sınıf
    def __init__(self, mesaj):
        self.mesaj = mesaj
try:
    raise ilkHatam("Bu benim ilk hatam")
except ilkHatam as hata:
    print ("Affedersiniz: ",hata.mesaj)
    print ("Modul: ", hata.ad)	
