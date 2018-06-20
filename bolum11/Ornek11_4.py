class Han():
    def __init__(self):
        self.zar = 1
        self._zar = 2
        self.__zar = 3
a = Han()
print (a._Han__zar) #Çıktı:3
print (Han().__dict__)
