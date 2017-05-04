# -*- coding: utf-8 -*-

import random

konum = [[0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0],
	 [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
x = input("x:")
y = input("y:")

def yangin(x,y):
    
    eleman = []
    for i in range(0,7):
	   for j in range(random.randint(0,2)):
	       eleman+=[j]
    if eleman == 1:
	konum[x][y] = eleman
    else:
	konum[x][y] = 0
    print(konum)
	   
       
print(yangin(x,y))

