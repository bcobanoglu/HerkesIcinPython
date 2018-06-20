#1-20 arası çift sayılar
def ciftS(sayi):
    return sayi%2==0
liste = range(1,20)
f_liste=filter(ciftS,liste)
print(list(f_liste))
#listeye dönüştürüp yazdırdık
