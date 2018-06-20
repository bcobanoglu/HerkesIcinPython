'''
Örnek 11.2.
Fibonacci serisini hesaplayan sınıf yapısını
‘init()’, ‘iter(), next()’ gibi özel metotlarla kodlayınız.
@author:Bülent Çobanoğlu
'''
'''fib2.py modulünden Fib sınıfını çağır'''
from fib2 import Fib
'''Fibonacci serisini (<5000) yazdır'''
for n in Fib(5000):
    print(n, end=' ')
