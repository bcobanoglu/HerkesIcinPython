'''
Örnek 5.5. 100’lük sisteme göre girilen başarı notunu harfli sisteme çeviren programı kodlayınız.
@author:Bülent Çobanoğlu
'''

# -*- coding: UTF-8 -*-
Nt=int(input('Gir Notu.:\n'))
if Nt >= 90:
    print ("AA")
elif Nt >= 80:
    print ("BA")
elif Nt >= 70:
    print ("BB")
elif Nt >= 60:
    print ("CB")
elif Nt >= 50:
    print ("CC")
else:
    print ("FF")
