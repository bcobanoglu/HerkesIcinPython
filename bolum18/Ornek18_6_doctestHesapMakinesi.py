'''
Örnek 18.6. Örnek 18.5’teki 4 işlem yapan programı doctest modülü ile gerçekleştiriniz.
author:Bülent Çobanoğlu
'''
def topla(a,b):
    """
    >>> topla(2, 3)
    5
    """
    return(a + b)

def carp(a,b):
    """
    >>> carp(2, 3)
    6
    """
    return(a * b)

def cikar(a,b):
    """
    >>> cikar(2, 3)
    -1
    """
    return(a - b)
def bol(a,b):
    """
    >>> bol(6, 3)
    2.0
    """
    return(a / b)

#doctest ana programı
if __name__ == "__main__":
    import doctest
    doctest.testmod()
