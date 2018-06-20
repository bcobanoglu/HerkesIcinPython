'''
Örnek 9.4. Girilen bir e-mail adresinin geçerli olup/olmadığını sorgulayan bir program yazınız.
@author:Bülent Çobanoğlu
'''
import re
email = input("e-mail adresini gir:")
rMailkontrol=r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$" #email kontrol stringi
m = re.search(rMailkontrol, email)

if m:
    print ("geçerli bir adres:", m.group())
else:
   print ("geçersiz bir adres, lütfen yeniden giriniz!!")
