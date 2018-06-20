'''
Örnek 4.9. Aşağıdaki programın çalıştırılmasından sonra d,e,f ve g değişkenlerinin içeriği ve ekran çıktısı ne olur?
'''
import operator
b=1
c=2
d= operator.and_(b,c) #b&c
e= operator.or_(b,c) #b|c
f= operator.rshift(c,1) #c>>1
g= operator.lshift(c,2) #c<<2
print (d,e,f,g)
