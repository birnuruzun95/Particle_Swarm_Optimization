# -*- coding: utf-8 -*-

import random

konum = [[0,0,0,0,0,0,0],
	 [0,2,0,2,0,2,0],
	 [0,0,0,0,0,0,0],
         [0,2,0,2,0,2,0],
         [0,0,0,0,0,0,0],
         [0,2,0,2,0,2,0],
         [0,0,0,0,0,0,0]]

oda = 9
t_alan = 49
yangin = 0

rastgele_yangin_sayisi = t_alan - oda - yangin

def yangin_olusturucu():
   global yangin
   while(yangin < rastgele_yangin_sayisi/5):
	x = random.randint(0,6)
	y = random.randint(0,6)
	if konum[x][y]!=2:
	   konum[x][y]=1
	   yangin+=1
	else:
	   continue 

yangin_olusturucu()

for i in range (0,7):
   print(konum[i])
  
#for i in range(0,7):
 #for j in range(random.randint(0,2)):
    # eleman+=[j]


