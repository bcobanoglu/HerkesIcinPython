#author:Bülent Çobanoğlu
#Soru 7.	Aşağıdaki programın ekran çıktısı ne olur?
import doctest

def us(a, b):
  """
  >>> us(2, 3)
  8
  >>> us('a', 2)
  'aa'
  """
  return a ** b


if __name__ == "__main__":
    doctest.testmod()
