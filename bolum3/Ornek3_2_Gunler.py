# -*- coding: UTF-8 -*-
from enum import Enum
gunler= Enum ('gunler', ['PZT', 'SAL', 'CAR', 'PER', 'CUM', 'CMT', 'PZR'])
print("Pazartesi: ", gunler.PZT.value)
print("Salı: ", gunler.SAL.value)
print("Çarşamba: ", gunler.CAR.value)
print("Perşembe: ", gunler.PER.value)
print("Cuma: ", gunler.CUM.value)
print("Cumartesi: ", gunler.CMT.value)
print("Pazar: ", gunler.PZR.value)
