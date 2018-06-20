'''
Örnek 6.14.
0-15 arasındaki sayıların;  onluk (decimal), ikilik (binary) ve onaltılık (hexadecimal) sayı sistemlerindeki karşılıklarını veren programı yazınız.
'''
print ("10\t2\t16")
print ("--\t--\t--")
for i in range(16):
    print(i, bin(i)[2:], hex(i)[2:], sep="\t")
