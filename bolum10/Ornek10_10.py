#author:bulend hoca
#Örnek 10.10. İki matrisi toplayan ve sonucu ekranda gösteren program

# -*- coding: UTF-8 -*-
A=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]
B=[
    [0, 2, 3],
    [4, 3, 5],
    [7, 1, 2],
  ]
C=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
  ]
# satirlarda gez
for i in range(len(A)):
    # sutunlarda gez
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]
for r in C:
    print(r)
