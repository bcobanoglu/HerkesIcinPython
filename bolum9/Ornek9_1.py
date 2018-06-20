'''
Örnek 9.1.
Verilen listeden adı ‘a’ veya ‘b’ ile başlayan ve ‘e’ ile biten isimleri
gösteren uygulamayı gerçekleştiriniz.
@author:Bülent Çobanoğlu
'''
import re
liste=["ali","ayşe","bade","sare","can"]
#adı a veya b ile başlayan ve e ile biten isimleri göster
for isim in liste:
    if re.search ("^[ab].*e$",isim):
        print(isim)
