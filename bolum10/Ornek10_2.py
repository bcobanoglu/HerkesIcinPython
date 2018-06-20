#0-24 arası Çift sayıları listele
#author:Bülent Çobanoğlu
L=[]
T=0
for i in range (24):
    if i%2==0:
        L.append(i)
        T=T+i
        print (L)
print ("Toplam=",T)
