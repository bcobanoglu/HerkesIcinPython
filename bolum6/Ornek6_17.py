'''
Örnek 6_17. Dik üçgen ve ters dik üçgenin birleşimi.
@author: Bülent Çobanoğlu
'''
for sat in range (1,10):
    for sut in range (1, 6-abs(5-sat)):
        print("*",end=' ')
    print("")
