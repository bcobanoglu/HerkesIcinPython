import pickle
sozluk = {'one':'bir', 'two': 'iki', 'three':'üç'}
with open('sozluk.dat', 'wb') as fh:
    pickle.dump(sozluk, fh)

print (pickle.load(open('sozluk.dat', 'rb')))

     