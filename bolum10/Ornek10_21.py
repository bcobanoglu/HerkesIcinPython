# -*- coding: UTF-8 -*-
#author-bulend hoca
derece = dict(ankara=3, istanbul=15.4, 
              bursa=7.5, bolu=-1)
#illeri sırala
print (list(sorted(derece)))
for il in derece:
    print (il, 'sıcaklık..:', derece[il])
