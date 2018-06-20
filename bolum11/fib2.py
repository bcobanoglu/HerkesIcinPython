class Fib:
  '''Yapılandırıcı sınıf:Fib(max)'''
  def __init__(self, max):
    self.max = max
  '''Yapılandırıcı sınıf:Fib(max)'''
  def __iter__(self):
    self.a = 0
    self.b = 1
    return self

  def __next__(self):
    fib = self.a
    #5000'e varmadan durdur
    if fib > self.max:
    raise StopIteration
    self.a= self.b
    self.b= self.a + self.b
    return fib
