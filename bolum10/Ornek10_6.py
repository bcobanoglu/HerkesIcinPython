# -*- coding: UTF-8 -*-
L =["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Agustos", "Eylül", "Ekim","Kasım","Aralık"]
ay=int(input("Kaçıncı ay..:"))
if ay>0 and ay<=12:
    print(ay,". ay..:"+ L[ay-1])
else:
    print("Hatalı ay numarasi!")

