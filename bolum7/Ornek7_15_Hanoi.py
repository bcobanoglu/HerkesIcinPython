#@author:Bülent Çobanoğlu
#Hanoi kuleleri oyunu
def hanoi(n, A, C, B):
    global s #s artık global değişken
    if n>0:
        hanoi(n-1, A, B, C)
        print(s,".adim:",A,"-->",C)
        s=s+1
        hanoi(n-1, B, C, A)
        return
#ana program
n = int(input('n degeri.:'))
s=1
#hanoi(n, 'kaynak', 'hedef', 'yedek')
hanoi(n, 'A', 'C', 'B')
