# mevlam.txt dosyası okuma amaçlı açıldı
#author:Bülend Hoca
f = open("mevlam.txt", "r")
print ("Dosya Adı: ", f.name)
print ("Okunan satır", f.readline())
pos = f.tell()
print ("işaretçinin pozisyonu: ", pos)
print ("Diğer satırlar:", f.read())
print ("işaretçinin pozisyonu: ", f.tell())
f.seek(0)#dosya başına dön
print ("işaretçinin son pozisyonu: ", f.tell())
f.close()
