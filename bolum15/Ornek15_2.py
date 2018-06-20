#author:Bülent Çobanoğlu
metin = '''Ben bir ağacım, içten kökten gülerim,
Aşk çeşmesi döndükçe sevincim de döner.
Mevlana'''
#dosya yazma amaçlı açıldı
f1 = open('mevla.txt', 'w')
f1.write(metin) #dosyaya metin yazıldı
f1.close() #dosya kapatıldı
