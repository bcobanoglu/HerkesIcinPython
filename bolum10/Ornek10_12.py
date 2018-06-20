#Bülend Hoca
A= [[1,2,3],
    [4,5,6],
    [7,8,9]]

#V= [i for matris in A for i in matris]
#print (V)

for matris in A:
    for i in matris:
        V=i
        print (i, end=" ")
