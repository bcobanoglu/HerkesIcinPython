# -*- coding: UTF-8 -*-
#author-Bülent Çobanoğlu
il = {} #boş il sözlüğü tanımlandı
#il sözlüğüne elemanlar ekleniyor
il['Ankara']='06'
il['Antalya']='07'
il['Erzincan']='24'
il['Sakarya']='54'
il['Tokat']='60'

plaka = {}#boş plaka sözlüğü tanımlandı
#plaka sözlüğüne elemanlar ekleniyor
plaka['01']='Adana'
plaka['25']='Erzurum'
plaka['67']='Trabzon'
plaka['16']='Bursa'

print('-' * 10)
# plaka sorgulaması yap
print("01 plakalı il.:", plaka.get('01'))
print('-' * 10)
# il sorgulaması yap
print("Ankara’nın plakası.:", il.get('Ankara'))
print('-' * 10)
