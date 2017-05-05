# -*- coding: utf-8 -*-

import random

konum = [[0,1,0,0,0,0,0],
	 [0,2,1,2,0,2,0],
	 [0,0,0,1,0,0,0],
         [0,2,0,2,0,2,1],
         [0,1,0,0,0,0,0],
         [0,2,1,2,0,2,0],
         [0,0,0,0,0,1,0]]
def matris_yazdir():
    for i in range (0,7):
        print(konum[i])
matris_yazdir()
#-------------------------------------------------------------------#

yangin_ym = [[0,0,0],
	     [0,0,0],
             [0,0,0],
             [0,0,0]]

def yangin_yatay():
    global yangin_ym
    i = 0
    j = 0
  
    print("yatay yangin matrisi:\n")
    for x in range(0,len(konum),2):	
	for y in range(1,len(konum[0]),2):
            yangin_ym[i][j] = konum[x][y]
            j += 1
	i += 1
	j = 0
    for k in range (0,len(yangin_ym)):
        print(yangin_ym[k])

print("\n")
yangin_yatay()
#------------------------------------------------------------------#

yangin_dm = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

def yangin_dikey():
    global yangin_dm
    i = 0
    j = 0
    print("dikey yangın matrisi:\n")
    for x in range(1,len(konum),2):
	for y in range(0,len(konum[0]),2):
	    yangin_dm[i][j] = konum[x][y]
            j += 1
	i += 1
	j = 0
    for k in range (0,len(yangin_dm)):
        print(yangin_dm[k])

print("\n")
yangin_dikey()
print("\n")
#------------------------------------------------------------------#

scdm_ym = [[0,0,0],
           [0,0,0],
           [0,0,0],
	   [0,0,0]]

def sicaklik_duman_yatay():
    global scdm_ym
    for x in range(0,len(scdm_ym)):
	for y in range(0,len(scdm_ym[0])):
	    if(yangin_ym[x][y] == 1): 
		if (y-1 >= 0):
		   scdm_ym[x][y-1]+=0.25
		if (y+1 <= len(scdm_ym[0])-1):
		   scdm_ym[x][y+1]+=0.25
		if (x-1 >= 0):
		   scdm_ym[x-1][y]+=0.25
		if (x+1 <= len(scdm_ym)-1):
                   scdm_ym[x+1][y]+=0.25
    for k in range (0,len(scdm_ym)):
        print(scdm_ym[k])

print("yatay sicaklik/duman matrisi:\n")
sicaklik_duman_yatay()
print("\n")
#------------------------------------------------------------------#
		
scdm_dm = [[0,0,0,0],
	   [0,0,0,0],
	   [0,0,0,0]]

def sicaklik_duman_dikey():
    global scdm_dm
    for x in range(0,len(scdm_dm)):
	for y in range(0,len(scdm_dm[0])):
	    if(yangin_dm[x][y] == 1): 
		if (y-1 >= 0):
		   scdm_dm[x][y-1]+=0.25
		if (y+1 <= len(scdm_dm[0])-1):
		   scdm_dm[x][y+1]+=0.25
		if (x-1 >= 0):
		   scdm_dm[x-1][y]+=0.25
		if (x+1 <= len(scdm_dm)-1):
                   scdm_dm[x+1][y]+=0.25
    for k in range (0,len(scdm_dm)):
        print(scdm_dm[k])

print("dikey sicaklik/duman matrisi:\n")
sicaklik_duman_dikey()
print("\n")
#------------------------------------------------------------------#	

isik_ym = [[1,1,1],
	   [0,0,0],
	   [0,0,0],
	   [1,1,1]]

print("yatay ışık matrisi:\n")
for k in range (0,len(isik_ym)):
    print(isik_ym[k])
print("\n")
#------------------------------------------------------------------#

isik_dm = [[1,0,0,1],
	   [1,0,0,1],
	   [1,0,0,1]]

print("dikey ışık matrisi:\n")
for k in range (0,len(isik_dm)):
    print(isik_dm[k])
print("\n")
#------------------------------------------------------------------#










