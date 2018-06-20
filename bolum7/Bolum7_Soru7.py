#sayısal loto
import random
def Loto():
    for i in range (6):
        sL=random.randint(1,50)
        print (sL, end=' ')
#Ana program
print("Sayısal Loto Çekilişi\n") 
Loto()



