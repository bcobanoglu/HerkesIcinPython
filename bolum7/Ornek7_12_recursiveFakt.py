#fakt fonksiyonu
def fakt(n):
    if n <= 1:
        return 1
    else:
        return (n * fakt(n-1))
#Ana program
n=int(input('Faktoriyel sayisi.:'))
print (n,"!=", fakt(n))
