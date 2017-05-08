# -*- coding: utf-8 -*-

import random

def matris_yazdir(matris):
   for i in range(0,len(matris)):
       print(matris[i])

konum = [[0,1,0,0,0,0,0],
	     [0,2,1,2,0,2,0],
	     [0,0,0,1,0,0,0],
         [0,2,0,2,0,2,1],
         [0,1,0,0,0,0,0],
         [0,2,1,2,0,2,0],
         [0,0,0,0,0,1,0]]

matris_yazdir(konum)
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
    matris_yazdir(yangin_ym)
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
    matris_yazdir(yangin_dm) 

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
    matris_yazdir(scdm_ym) 

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
    matris_yazdir(scdm_dm) 

print("dikey sicaklik/duman matrisi:\n")
sicaklik_duman_dikey()
print("\n")
#------------------------------------------------------------------#	

isik_ym = [[1,1,1],
	       [0,0,0],
	       [0,0,0],
	       [1,1,1]]

print("yatay ışık matrisi:\n")
matris_yazdir(isik_ym)
print("\n")
#------------------------------------------------------------------#

isik_dm = [[1,0,0,1],
	       [1,0,0,1],
	       [1,0,0,1]]

print("dikey ışık matrisi:\n")
matris_yazdir(isik_dm) 
print("\n")
#------------------------------------------------------------------#

mesafe = 13

result_ym = [[0,0,0],
             [0,0,0],
             [0,0,0],
	         [0,0,0]]

def result_yatay():
    global result_ym
    for x in range(0,len(result_ym)):
        for y in range(0,len(result_ym[0])):
            result_ym[x][y] = float(2*mesafe + (scdm_ym[x][y]/mesafe) - (1.5*isik_ym[x][y]))

result_yatay()
print("yatay ara sonuç  matrisi:\n")
matris_yazdir(result_ym)
print("\n")
#------------------------------------------------------------------#

result_dm = [[0,0,0,0],
	         [0,0,0,0],
	         [0,0,0,0]]


def result_dikey():
    global result_dm
    for x in range(0,len(result_dm)):
        for y in range(0,len(result_dm[0])):
            result_dm[x][y] = float(2*mesafe + (scdm_dm[x][y]/mesafe) - (1.5*isik_dm[x][y]))

result_dikey()
print("Dikey Ara Sonuç Matrisi:")
matris_yazdir(result_dm)
print("\n")

#-----------------------------------------------------------EOF-:)--#
 







