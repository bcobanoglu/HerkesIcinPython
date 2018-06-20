'''from time import strftime, strptime, gmtime
tarih=("1974, 10, 17, 12, 45")
print (strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
#print (tarih.strftime("%c"))
#print (tarih.strftime("%c") )
@author:Bülent Çobanoğlu
'''
import time
suAn = time.asctime()
#alternatifi
#suAn = time.ctime()
print (suAn)

date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
suan2= time.mktime(date1)
print(suan2)
