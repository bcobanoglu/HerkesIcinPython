'''
Örnek 13.3. Bir kaplumbağa robotunu merdivenden 5 basamak aşağı indiren
(veya 5 basamaktan oluşan bir merdiven şeklini ekrana çizen) uygulamayı kodlayınız.
@author:Bülent Çobanoğlu
'''
from turtle import *
#kaplumbağa çiz
shape('turtle')
for i in range(5):
    forward(50) 
    left(90)
    forward(50)
    left(90)
