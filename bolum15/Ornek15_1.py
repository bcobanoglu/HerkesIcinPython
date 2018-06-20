#author:Bülent Çobanoğlu
f = open("mevla.txt", "r")
print ("Dosya Adı: ", f.name)
print ("Kapalı mı Açık mı? : ", f.closed)
print ("Açılış amacı : ", f.mode)
f.close()
print ("Kapalı mı Açık mı? : ", f.closed)
