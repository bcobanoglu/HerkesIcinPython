'''
Örnek 8.13. Dosya ismini sorgulayan uygulama:
Girilen bir dosya isminin uzantısına bakarak (.py) o dosyanın bir Python programı olup olmadığını bulan programı yazınız.
'''
# -*- coding: UTF-8 -*-
s=input("Dosya adı..:")
s1 = s[len(s)-3:len(s)] #son 3 karakteri al
if s1.lower()== '.py':
    print ("Bu bir Python programıdır.")
else:
    print ("Bu bir Python programı değildir")
