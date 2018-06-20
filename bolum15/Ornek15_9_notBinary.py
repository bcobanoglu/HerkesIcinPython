#author:Bülent Çobanoğlu
import pickle
notlar= ["Ömer Can :90", "Berat Can :95",
         "Levent Çoban :100", "Bade Zehra :50",
         "Ekrem Can :68" ]
#ikili dosya yazma amaçlı açıldı ve notlar yazıldı
with open('notlar.bin', 'wb') as f:
    pickle.dump(notlar,f)
#şimdi dosyayı açıp, okuyalım.
with open('notlar.bin', 'rb') as f:
    notList=pickle.load(f)
    print(notList )
