#@author:Bülent Çobanoğlu
#Özyinelemeli Fibonacci serisi
def fib(n):
    a, b = 0, 1 #a=0,b=1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b #a=b,b=a+b oldu
#Ana program
fib(1000)
