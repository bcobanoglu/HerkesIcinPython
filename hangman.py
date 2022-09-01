import random  #random modülü import ediliyor
import os
from nltk import flatten
import pandas as pd

# tdk kelime listesini tutan dosya
url = "https://raw.githubusercontent.com/bcobanoglu/HerkesIcinPython/master/tdk_kelime_list.txt"
df = pd.read_csv(url)
liste = flatten(df.sample(10).values.tolist()) # tdk sözlüğünden 10 kelime al
print(liste)
kelime = random.choice(liste)                  # birini seç

#her yanlış harfte ekranda gösterilecek 7 elemanlı hangman listesi 
hangman = ['''
  +----+
  o    |
 -|-   | 
 / \   |
     _===_
''','''
  +----+
  o    |
 -|-   | 
 /     |
     _===_
''','''
  +----+
  o    |
 -|-   | 
       |
     _===_
''','''
  +----+
  o    |
 -|    | 
       |
     _===_
''','''
  +----+
  o    |
  |    | 
       |
     _===_
''','''
  +----+
  o    |
       | 
       |
     _===_
''','''
  +----+
       |
       | 
       |
     _===_
''']
dogruHarf = []              # doğru harf listesi
yanlisHarf = []             # yanlış harf (hatalı durum) listesi
hak = len(hangman)          # hangman eleman sayısı kadar hak verilir
while hak>0:                # hak sıfırdan büyük olduğu sürece
    out=""                  # çıktı değişkeni
    for h in kelime:        # kelimenin harfleri üzerinde dolaşalım
        if h in dogruHarf:  # doğru harf ise 
            out = out + h   # çıktıya o harfi ekle
        else:               # yanlış harf ise 
            out = out + "_" # çıktıya _ ekle
    if out == kelime:       # çıktı, seçilen kelimeye eşitse
        break               # döngüden çık
    print ("Kelime: ", out) # Mevcut çıktıyı yaz
    print (hangman[hak-1])  # listedeki görseli yaz
    girHarf = input()       # harf gir ve girilen harfi karşılaştır
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print ("zaten ", girHarf, "girilmişti!")
    elif girHarf in kelime:
        print ("Doğru")
        dogruHarf.append(girHarf) #dogruHarf listesine ekle
        os.system('clear')  # ekranı temizle
    else:                   # girilen harf kelimede yoksa
        print ("Yanlış")
        hak = hak -1        # hakkı 1 azalt 
        yanlisHarf.append(girHarf) #yanlisHarf listesine ekle
       
if hak !=0:                 # hak bitmeden çıkıldı ise Tebrikler 
    print ("Tebrikler, Evet:", kelime)
else:
    print ("Maalesef kelimemiz:", kelime)