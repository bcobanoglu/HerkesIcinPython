'''
Örnek 6.16. Ekrana 1’den 7’ye ve 7’den 1’e kadar ‘*’ karakterlerinden oluşan dik üçgeni ve ters dik üçgeni çizen programları yazınız.
@author: Bülent Çobanoğlu
'''
#Dik üçgen
for i in range (7):
    for j in range (i+1):
        print("*",end=' ')
    print("")

#Ters Dik üçgen
for i in range (7, 0, -1):
    for j in range (i, 0, -1):
        print("*",end=' ')
    print("")
