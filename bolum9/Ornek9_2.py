'''
Örnek 9.2.
Bir metin içerisindeki kelimeleri başka bir kelime ile değiştiren uygulamayı gerçekleştiriniz
@author:Bülent Çobanoğlu
'''
import re
tekerleme= """kartal kalkar, dal sarkar, dal sarkar, kartal kalkar."""
degistir=re.sub("sarkar","kalkar",tekerleme)
print(degistir)
