#author:Bülend Hoca
#yin-yang simgesi
from turtle import *
shape("blank") #kaplumbağayı gizle
def yinYang(r, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()#boyama başla
    circle(r/2.0, 180)
    circle(r, 180)
    left(180)
    circle(-r/2.0, 180)
    end_fill()#boyamayı bitir
    left(90)
    penup() #up() kalemi kaldır
    forward(r*0.35) #ileri git
    right(90)
    pendown() #down()kalemi bastır
    color(color1, color2)
    begin_fill()#boyamaya basla
    circle(r*0.15)
    left(90)
    backward(r*0.35) #geri git
    left(90)
    end_fill()#boyamayı bitir

def main():
    reset()
    yinYang(100, "white", "black")
    yinYang(100, "black", "white")

if __name__ == '__main__':
    main()
