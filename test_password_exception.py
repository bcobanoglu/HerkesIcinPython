# -*- coding: utf-8 -*-

# Önce password üreteci yapalım sonra da test edelim
import random
import re

def pass_generator():
    sifre = ""
    for i in range(8):
        sifre = sifre + chr(random.randint(33,127))
    return sifre
# test fonksiyonu

def check_password(psw):
    """
        # bu  password_generator() fonksiyonu test eden fonksiyon yazalım
        # en az 8 karakter mi
        # en az bir küçük harf
        # en az bir büyük harf
        # en az bir rakam
        # en az bir punctation içeriyor mu? test edelim...
    """
    if len(psw)<8:
        raise Exception("Password 8 karakterden az olamaz")
    elif not re.search("[a-z]", psw):
        raise Exception("Password en az bir küçük harf içermeli")
    elif not re.search("[A-Z]", psw):
        raise Exception("Password en az bir büyük harf içermeli")
    elif not re.search("[0-9]", psw):
        raise Exception("Password en az bir rakam içermeli")
    elif not re.search("[!#$%&'()*+,-./:;<=>?@[\]^_\"{|}~.]", psw):
        raise Exception("Password en az bir özel simge içermeli")

#main program
try:
    sifrem = pass_generator()
    print(sifrem)
    check_password(sifrem)
except Exception as ex:
    print(ex)
else:
    print("Password geçerli")
finally:
    print("Test başarılı!!")
