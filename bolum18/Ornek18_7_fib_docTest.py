#author:Bülent Çobanoğlu
import doctest

def fib(n):
    """
    Fibonacci serisinin n.elemanı veren fonksiyon:
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
    >>> fib(13)
    233
    >>>
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b #a=b,b=a+b oldu
    return a

if __name__ == "__main__":
    doctest.testmod()
