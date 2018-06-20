'''
Örnek 8.8. Cümledeki kelime ve harf sayısını öğrenme: Girilen bir cümledeki harflerin ve kelimelerin sayısını veren programı yazınız.
@author: Bülent Çobanoğlu
'''
# -*- coding: UTF-8 -*-
cumle=input ('Cumle gir..:')
kSay=cumle.count(" ")
hSay=len(cumle)-kSay
print ("Kelime sayısı..:", kSay+1)
print ("Harf sayısı..:",hSay)	
