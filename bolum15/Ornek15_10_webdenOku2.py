import urllib.request
#Text içerikli bir web adresi gir
adres = "http://shallowsky.com/python/lesson5.txt"
#web adresini aç
f = urllib.request.urlopen(adres)
# Okuduğunu string formatında dosya değişkeninde tut
dosya = f.read().decode() 
#dosya değişkeninin içeriğini ekrana yaz
print (dosya)
