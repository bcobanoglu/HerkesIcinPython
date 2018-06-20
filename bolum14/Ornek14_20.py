from PIL import Image #PIL kütüphanesini ekler
resim1 = Image.open('oglan.gif') # resimi yükle
resim1.show() # orjinal resimi göster

box = (150, 200, 600, 600)
resim2 = resim1.crop(box) #resimi kırpar
resim2.save('kirp.bmp') #resim2'yi kaydet
resim2.show() #resim2'yi göster

resim3 = resim1.resize((250, 400)) #resimin yeni boyutu
x=resim3.rotate(90) #resimYeni'yi 90 derece döndürür
y=x.convert('L') #x'e L(greyscale-gri ton) moduna dönüştürür.
y.save('oglan.png') #y'yi 'oglan.png' olarak kaydeder.
y.show() #y'yi ekranda gösterir

print("resim1 uzantısı:",resim1.format) # Resim dosyasının uzantısını verir.
print("resim1 modu:",resim1.mode) #Resim1'in Pixel formatını(“P”, “L”, “RGB”, veya “CMYK”) verir
print("resim1 boyutu:", resim1.size) #Resim boyutunu pixel olarak verir(genişlik, yükseklik)
print("resim2 boyutu:",resim2.size)
print("resim2 uzantısı:",resim2.format)
print("resim3 boyutu:",y.size)
print ("resim3 modu:",y.mode)
