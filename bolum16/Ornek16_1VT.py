'''
Örnek 16.1. Öncelikle ‘personel.db’ isminde bir veri tabanı oluşturunuz.
Sonrasında ise bu veri tabanı içerisinde ‘no, ad, adres’
alanlarından oluşan bir ‘perTablo’ isimli tablo oluşturup, bu tablo üzerinde sorgulamalar gerçekleştiriniz.
@author:Bülent Çobanoğlu
'''
import sqlite3 #sqlite modülü çağrıldı
bgln = sqlite3.connect("personel.db") #personel.db isimli veri tabanı tanımlandı
imlec = bgln.cursor() #imlec (kürsor) nesnesi oluşturuldu

#Eğer perTablo önceden oluşturuldu ise silinsin
imlec.execute('drop table if exists perTablo;')
#perTablo isimli tablo oluşturuldu
imlec.execute("""CREATE TABLE perTablo
(no INTEGER PRIMARY KEY, ad TEXT, adres TEXT)""")
#kayıtlar listesi
kayitlar=[(1, 'Zehra', 'Tokat'),
          (2, 'Levent', 'İstanbul') ]
#kayıtlar listesini perTablo'ya ekle.
imlec.executemany('INSERT INTO perTablo VALUES (?,?,?)', kayitlar)

#perTablo'ya yeni kayıtlar eklendi
imlec.execute("INSERT INTO perTablo values"
             " (3, 'Bade', 'Tokat')")
imlec.execute("INSERT INTO perTablo values"
             " (4, 'Berat', 'Sakarya')")
imlec.execute("INSERT INTO perTablo values (5, 'Omer', 'Amasya')")

bgln.commit() #veri tabanı güncellendi
#bir döngü içerisinde tüm kayıtlar ada göre listelendi
print("personel.db içindeki perTablo kayıtları Ad'a göre listelendi.")
for kyt in imlec.execute('SELECT * FROM perTablo ORDER BY ad'):
        print(kyt)

bgln.close() #veri tabanı kapatıldı
