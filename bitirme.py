# -*- coding: utf-8 -*-

import random

konum = [[0,0,0,0,0,0,0],
	 [0,2,0,2,0,2,0],
	 [0,0,0,0,0,0,0],
         [0,2,0,2,0,2,0],
         [0,0,0,0,0,0,0],
         [0,2,0,2,0,2,0],
         [0,0,0,0,0,0,0]]

x = random.randint(0,1)
y = random.randint(0,1)

def yangin(x,y):
    
   if konum[x][y]==2:
      print("ROOM") 
   elif konum[x][y]==0: 
       
      deger = random.randint(0,1)  
      konum[x][y] = deger

   else:
      print("Fire!")
    
    #for i in range(0,7):
	   #for j in range(random.randint(0,2)):
	      # eleman+=[j]
   for i in range (0,7):
     print(konum[i])

yangin(x,y)

