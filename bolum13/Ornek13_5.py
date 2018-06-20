'''
Örnek 13.5. 2017 yılı itibari ile Erzincan, Erzurum, Eskişehir, Tokat ve Sakarya illerinin yaklaşık nüfusu sırası ile 231.511,760.476, 860.620, 602.086 ve 990.214’ dir.
Bu illerin nüfusunu grafiksel olarak gösteren programı yazınız.
@author:Bülent Çobanoğlu
'''
from turtle import *
#illerin nüfusu
nfs=[231.511,760.476,860.62,602.086,990.214] goto(0,-200) #sety(-200)

def cizBar(height):
    left(90) #sola dön
    forward(height/10)# Sol kenarı çiz
    #nüfus değerlerini yaz
    write(" "+ str(height))
    right(90) #sağa dön
    forward(44)#sağ kenar:bar genişliği
    right(90) #sağa dön
    forward(height/10) #tekrar aşağı in!
    left(90)  # sola dön

pensize(3) #çizgi kalınlığı
begin_fill() #boyamaya başla
#çizgi rengi mavi, bar içi kırmızı
color("blue", "gray")
write("Erzincan- Erzurum- Eskishr- Tokat   - Sakarya")
for v in nfs:
    cizBar(v)
end_fill() #boyamayı sonlandır
