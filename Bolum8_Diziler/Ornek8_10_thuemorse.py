# -*- coding: UTF-8 -*-
#Thue-Morse Uygulaması
#author:Bülent Çobanoğlu
m='0'
print(m)
for i in range(0,5):
    m0=m
    m=m.replace('0','b')
    m=m.replace('1','0')
    m=m.replace('b','1')
    m=m0+m
    print(m)

"""
0
01
0110
01101001
0110100110010110
01101001100101101001011001101001
0110100110010110100101100110100110010110011010010110100110010110
"""
