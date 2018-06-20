# -*- coding: UTF-8 -*-
#author-bulend hoca
aranan=input("Gun degeri..:")
enTr={"monday":"pazartesi","tuesday":"salı", 
    "wednesday":"çarşamba","thursday":"perşembe", 
    "friday":"cuma","saturday":"cumartesi",
    "sunday":"pazar"}
print(enTr.get(aranan, "Bu kelime sözlükte yoktur!"))
