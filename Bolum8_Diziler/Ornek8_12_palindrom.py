#Örnek 8.12. Palindrom Uygulaması
#author:Bülent Çobanoğlu
# -*- coding: UTF-8 -*-
s=input("Bir metin gir.:")
if s == ''.join(reversed(s)): #if(s==s[::-1]):
    print(s, ":palindrom")
else:
    print(s, ":palindrom degil")
