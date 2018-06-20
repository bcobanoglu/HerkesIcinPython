'''
Örnek 6.18: 1-0 lardan oluşan 5*11 matris
@author: Bülent Çobanoğlu
'''
N=5
for a in range (N):
    for b in range (2*N+1):
        if b<N-a or b>N+a:
            print ("1",end=' ')
        else:
            print ("0",end=' ')
    #b dongusu sonu
    print ("\n")
#a dongusu sonu
