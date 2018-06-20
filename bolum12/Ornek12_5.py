'''
Örnek 12.5. Girilen bir sayının karesini alan programı yazınız
@author:Bülent Çobanoğlu
'''
while True: #Sonsuz döngü
    try:
        x = int(input("Bir sayi gir..: "))
        print ("x^2=",x*x)
        break #döngüyü sonlandır
    except ValueError: #Değer hatası
        print("Bu bir sayi degil!!!")
