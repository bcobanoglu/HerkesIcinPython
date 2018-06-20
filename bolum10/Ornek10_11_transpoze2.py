#author:bulend hoca
# -*- coding: UTF-8 -*-
#Matrisin transpozesi
A=[
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 0, 4],
  ]
B = [] 
B=list(zip(*A))
print("Transpozesi:",B)
