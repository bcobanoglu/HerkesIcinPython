"""
Klasik Nokia Yılan Oyunu
Author: Bülent Çobanoğlu
Kaynak: https://www.edureka.co/blog/python-turtle-module/
"""
import turtle
import time
import random
#Değişkenler ve başlangıç değerleri
bekle = 0.1 #gecikme değişkeni
skor = 0 #Skor değişkeni
maxSkor = 0 #max. skor değişkeni
Liste = [] #dizi
#Ekran ayarları
wn = turtle.Screen() #oyun alanı çerçeve değişkeni: wn
wn.title("Yılan oyunu") #çerçeve başlığı
wn.bgcolor("green") #çerçeve arka planı: yeşil
wn.setup(600, 600) #çerçeve boyutu
wn.tracer(0) #ekranı güncellemesi kapalı

#Yılan nesnemizi oluşturup, özelliklerini belirliyoruz
yln= turtle.Turtle() #yılan nesnesi (değişkeni):yln 
yln.speed(0) #yılanın başlangıç hızı
yln.shape("square") #yılanın şekli: kare
yln.color("yellow") #yılanın rengi: sarı
yln.penup() #Kalemi kaldır. Hareket ederken çizgi çizme
yln.goto(0, 100) #yılanın başlangıç konumu
yln.yonu = "dur" #sabit dur, hareket etme!

#Yem nesnesini oluşturup, başlangıç ayarlarını yapıyoruz
yem = turtle.Turtle() #Yem nesnesi (değişkeni): yem
yem.speed(0) #yemin başlangıç hızı
yem.shape("circle") #yemin şekli: daire
yem.color("white") #yemin rengi: beyaz
yem.penup() #Kalemi kaldır
yem.goto(0,0) #Yemin başlangıç konumu

# Fonksiyonlar
def gitYukari():
    if yln.yonu != "alt":
        yln.yonu = "ust"
def gitAsagi():
    if yln.yonu != "ust":
        yln.yonu = "alt"
def gitSola():
    if yln.yonu != "sag":
        yln.yonu = "sol"
def gitSaga():
    if yln.yonu != "sol":
        yln.yonu = "sag"

def Hareket():
    if yln.yonu == "ust":
        y = yln.ycor() #y ekseninde yukarı hareket et
        yln.sety(y + 20) #20 birim ilerle
 
    if yln.yonu == "alt":
        y = yln.ycor() #y ekseninde aşağı hareket et
        yln.sety(y - 20) #20 birim ilerle
 
    if yln.yonu == "sag":
        x = yln.xcor() #x ekseninde sağa doğru hareket et
        yln.setx(x + 20) #20 birim ilerle
 
    if yln.yonu == "sol":
        x = yln.xcor() #x ekseninde sola doğru hareket et
        yln.setx(x - 20) #20 birim ilerle
#yemiYe() fonksiyonu
def yemiYe():
    global bekle, skor, maxSkor
    #Yılan yeme 20 birimden az yaklaşırsa
    if yln.distance(yem) < 20:
        # Yemi çerçeve içerisinde rastgele bir noktaya konumla
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x,y)

        #Kuyruk nesnesini oluşturalım
        kuyruk = turtle.Turtle() #kuyruk nesnesi
        kuyruk.speed(0) #kuyruğun başlangıç hızı
        kuyruk.shape("square") #kuyruğun şekli:kare
        kuyruk.color("red") #kuyruğun rengi:kırmızı
        kuyruk.penup() #kalemi kaldır
        Liste.append(kuyruk) #kuyruğu listeye ekle

        # Kuyruk uzadıkça hızı biraz yavaşlatalım
        bekle = bekle - 0.001
        # Her başarılı yemede puanı 10 puan artır
        skor = skor + 10
        #Eğer skor, maxSkor dan büyükse skoru maxSkor yap.
        if skor > maxSkor:
            maxSkor = skor
        #skor değerlerini anlık çerçeve başlığında göster
        wn.title("Skor: {}  En yüksek skorun: {}".format(skor, maxSkor))
    
    # Listeyi ters sırada hereket ettirelim
    uz = len(Liste) #listenin uzunluğunu (kuyruk sayısını) al
    for indis in range(uz-1, 0, -1): #ters sırada
        x = Liste[indis-1].xcor()
        y = Liste[indis-1].ycor()
        Liste[indis].goto(x, y)
   
    #Listenin ilk elemanını yılanın başı olur
    if len(Liste) > 0: 
        x = yln.xcor()
        y = yln.ycor()
        Liste[0].goto(x,y)

def baslangicAyarlari():
    time.sleep(1)
    yln.goto(0,0)
    yln.yonu = "dur"
    global skor
    #Yılanın eklemlerini çerçeve dışına taşı
    for eklem in Liste:
        eklem.goto(1000, 1000)
    Liste.clear() # ve listeyi temizle
    skor = 0 #skoru sıfırla
    bekle= 0.1 #gecikmeyi sıfırla
    # Skoru güncelle
    wn.title("Skor: {}  En yüksek skorun: {}".format(skor, maxSkor))

# Klavye olaylarını dinle
wn.listen()
wn.onkeypress(gitYukari, "Up")
wn.onkeypress(gitAsagi, "Down")
wn.onkeypress(gitSola, "Left")
wn.onkeypress(gitSaga, "Right")

#Ana oyun döngüsü
while True:
    wn.update()
    yemiYe()
    Hareket()    
    #Yılan köşelere çarpınca
    if yln.xcor()>290 or yln.xcor()<-290 or yln.ycor()>290 or yln.ycor()<-290:
        baslangicAyarlari()
    #veya yılan kendi vücuduna çarparsa
    for eklem in Liste:
        if eklem.distance(yln) < 20:
            baslangicAyarlari()
    time.sleep(bekle) #belli bir süre bekle

wn.mainloop() #olay yakalama döngüsü aktif