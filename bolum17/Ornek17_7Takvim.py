'''
Örnek 17.7. Takvim Uygulaması: Girilen bir yıla ait takvimi
Türkçe olarak listeleyen programı yazınız.
@author:Bülent Çobanoğlu
'''
import calendar
yil = int(input("Takvim yılını giriniz:"))
cal=calendar.LocaleTextCalendar(0,"TURKISH") # Bir takvim nesnesi oluştur
cal.pryear(yil) #alternatifi: print(calendar.prcal(yil))
