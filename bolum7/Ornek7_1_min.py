'''
Örnek 7.1.  Girilen üç sayı içerisinden en büyük ve en küçük olanları bulup ekranda gösteren programı yazınız.
@author: Bülent Çobanoğlu
'''
a,b,c=3,15,9
def enb (x, y, z):
    return max(max(x,y),z)
def enk (x, y, z):
    return min(min(x,y),z)
#Ana program
print("En buyugu:", enb(a,b,c))
print("En kucugu:", enk(a,b,c))
