
#@author:Bülent Çobanoğlu
import sqlite3
print("SQLite veritabanı sürümü..:", sqlite3.version)
print("SQLite3 kütüphane sürümü..:", sqlite3.sqlite_version)
bgln = sqlite3.connect('personel.db')
vt = bgln.cursor()
'''sorgu1:'Adı 'Levent' olan kaydı 'Bulent' olarak güncelle/değiştir'''
sorgu1=vt.execute("update perTablo set ad='Bulent' where ad='Omer'")
#Adı 'B' ile başlayanları listele
sorgu2 = vt.execute('SELECT DISTINCT ad FROM perTablo WHERE ad LIKE "B%"')
for kayitlar in sorgu2:
    print(kayitlar)

bgln.commit() #veritabanını kayde
bgln.close() #veritabanını kapat
