'''
Örnek 12.7. try-except-else kullanım örneği
@author:Bülent Çobanoğlu
'''
try:
    x = int(input("x= "))
    y = int(input("y= "))
except:
    print("Hata olustu!!!")
    #standat hata mesajı
else:
    print(x/y)
