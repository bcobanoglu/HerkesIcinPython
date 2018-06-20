'''
Örnek 17.6. 3’er saniye aralıklarla 3 kez beşgen çizen programı yazınız.
@author:Bülent Çobanoğlu
'''
import turtle
import time
def cizBesgen():
    tostos = turtle.Turtle()
    aci = 360/5
    tostos.pensize(2)
    for i in range(5):
        tostos.forward(50)
        tostos.left(aci)
    time.sleep(3)

#Ana program
#3 er saniye aralıklarla
cizBesgen()
cizBesgen()
cizBesgen()
