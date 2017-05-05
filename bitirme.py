# -*- coding: utf-8 -*-

import random

konum = [[0,1,0,0,0,0,0],
	 [0,2,1,2,0,2,0],
	 [0,0,0,1,0,0,0],
         [0,2,0,2,0,2,1],
         [0,1,0,0,0,0,0],
         [0,2,1,2,0,2,0],
         [0,0,0,0,0,1,0]]

#for i in range (0,7):
#   print(konum[i])

yangin_ym = []

def yangin_yatay():
    global yangin_ym
    for x in range(0,7):
       if x%2==0:
	  for y in range(0,7):
    	      if y%2==0:
	          y+=1
	          continue
       	      elif y%2!=0:
	          yangin_ym = konum[x][y]
	          print(yangin_ym)
                  
       else:
         x+=1

def yangin_dikey():
    global yangin_ym
    for x in range(0,7):
       if x%2!=0:
	  for y in range(0,7):
    	      if y%2!=0:
	          y+=1
	          continue
       	      elif y%2==0:
	          yangin_ym = konum[x][y]
	          print(yangin_ym)
                  
       else:
         x+=1
print("\n")
yangin_dikey()
print("\n")
yangin_dikey()
