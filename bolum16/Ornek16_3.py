#author:Bülent Çobanoğlu
import sqlite3
bgln = sqlite3.connect('personel.db')
vt = bgln.cursor()
#Eğer perTablo önceden oluşturuldu ise silinsin
vt.execute('drop table if exists perTablo;')
vt.execute("""CREATE TABLE perTablo
(no INTEGER PRIMARY KEY, ad TEXT, adres TEXT)""")
#kayıtlar listesi
kayitlar=[(1, 'Zehra', 'Tokat'),
          (2, 'Levent', 'İstanbul'),
          (3, 'Erkam', 'Eskişehir')
         ]
#kayıtlar listesini perTablo'ya ekle.
vt.executemany('INSERT INTO perTablo VALUES (?,?,?)', kayitlar)

#'perTablo' ismini 'insanlar' olarak değiştir
vt.execute("ALTER TABLE perTablo RENAME TO insanlar;")
#insanlar tablosunun sadece ad ve adres alanlarını listele

vt.execute("DELETE FROM insanlar WHERE no=3;")
#Tablodan no=3 olan kayıtları siler

sorgu2 = vt.execute('SELECT ad, adres FROM insanlar ')
for kayitlar in sorgu2:
    print(kayitlar)

# İstereseniz tablo ismini tekrar eski haline getirebilirisiniz!
# vt.execute("ALTER TABLE insanlar RENAME TO perTablo;")

bgln.commit() #veritabanını kayde
bgln.close() #veritabanını kapat
