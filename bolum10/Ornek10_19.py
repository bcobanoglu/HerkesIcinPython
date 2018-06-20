'''
Örnek 10.19.
0’dan 24’e kadar ki çift sayıların karesini sözlük yapısını kullanarak kodlayınız.
@author:Bülent Çobanoğlu
'''
S= {x: x**2 for x in range(0,24) if x%2==0}
print(S)
