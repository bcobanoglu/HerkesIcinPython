'''
Örnek 17.4. Geçmiş tarihi bulan/hesaplayan bir program yazınız.
@author:Bülent Çobanoğlu
'''
from datetime import date, timedelta
tarih1 = date.today()
print ("Bugünkü Tarih:",tarih1)
gun= int(input("Geçmiş günü gir:"))
gecmis = timedelta(days=gun)
tarih2 = tarih1 - gecmis
print (tarih2.strftime('%x'))
