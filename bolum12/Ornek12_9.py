'''
Örnek 12.9. raise ile bilerek hata mesajı üreten bir uygulama örneği
@author:Bülent Çobanoğlu
'''
kat = int(input("hangi kata çıkacaksınız: "))
if kat == 13:
    raise NameError("Bu kata çıkamazsınız!")
print("Asansör", kat, "a çıkıyor")
