'''
Örnek 12.8. try-except-finally kullanım örneği
@author:Bülent Çobanoğlu
'''
try:
    x = int(input("x= "))
    y = int(input("y= "))
    print(x/y)
except:
    print("Hata olustu!!!")
finally:
    print ("Hatasız günler dilerim..")
