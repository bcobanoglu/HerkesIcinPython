'''
Örnek 9.3.
Bir metin içerisinde sonu ‘olur’ ile biten kelimelerden
yeni bir liste oluşturan uygulamayı gerçekleştiriniz.
@author:Bülent Çobanoğlu
'''
import re
siir= """sanma şâhım herkesi sen sadıkâne yâr_olur
       herkesi sen dost mu sandın belki ol ağyâr_olur
       sadıkâne belki ol âlemde serdâr_olur
       yâr olur ağyâr olur serdâr olur dîldâr_olur
       Yavuz Sultan Selim"""
sonOlur=re.findall("\w+olur",siir) #sonu ‘olur’ ile biten kelimeleri al
print(sonOlur)
