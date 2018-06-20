'''
Örnek 4.3. Aşağıdaki program parçasının ekran çıktısı ne olur? Özellikle çoklu atama işlemlerine dikkat ediniz.
'''
b = c = 2
a = 4
a /= b #a=a/b
print(a, b, c)
a -= b #a=a-b
print(a, b, c)
