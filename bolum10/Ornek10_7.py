#author-bulend hoca
A=[];B=[]
#Asal sayiyi bulan fonksiyon
def isAsal(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
#Ana program
for n in range(0,35):
    if isAsal(n)==True:
        A+=[n]
    else:
        B+=[n]
print("Asal olanlar..:",A)
print("Asal olmayanlar..:",B)
