#author:Bülend Hoca
from turtle import *

shape('turtle')
#Çizim ekran boyutu
setup(500,500)

# yön tuşları fonksiyonları
def gitSola():
    left(10)
    write("Sola dön!", font=('Arial',9))
def gitSaga():
    right(10)
    write("Sağa dön!", font=('Consolas',8))
def gitIleri():
    forward(20)

def gitGeri():
    backward(20)

# Tuş fonksiyonları
onkeypress(gitSola, 'Left')
onkeypress(gitSaga, 'Right')
onkeypress(gitIleri, 'Up')
onkeypress(gitGeri, 'Down')

# basılan tuşu dinle
listen()
#olay yakalama döngüsü
mainloop() #done
