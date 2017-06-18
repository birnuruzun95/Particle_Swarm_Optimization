# -*- coding: utf-8 -*-
import matrix_and_neo as mn
#import matplotlib.pyplot as plt
import numpy as np
import random as rand

def matrix():
    i = 0
    j = 0
    for x in range(0, len(mn.konum), 2):
        for y in range(1, len(mn.konum[0]), 2):
            mn.konum[x][y] = mn.result_ym[i][j]
            j += 1
        i += 1
        j = 0
    i = 0
    j = 0
    for x in range(1, len(mn.konum), 2):
        for y in range(0, len(mn.konum[0]), 2):
            mn.konum[x][y] = mn.result_dm[i][j]
            j += 1
        i += 1
        j = 0
    print("elde edilen metrik değerleri:")
    mn.matris_yazdir(mn.konum)

def parcacik():
    matrix()
    distance = []
    best = []
    visited = [[]]
    c = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    startnode = raw_input("Lütfen bulunduğunuz konumu ifade eden, 1-16 arasında bir konum  değeri giriniz:")

    if startnode == "1":
        i=0
        j=6
    elif startnode == "2":
        i=2
        j=6
    elif startnode == "3":
        i=4
        j=6
    elif startnode == "4":
        i=6
        j=6
    elif startnode == "5":
        i=0
        j=4
    elif startnode == "6":
        i=2
        j=4
    elif startnode == "7":
        i=4
        J=4
    elif startnode == "8":
        i=6
        j=4
    elif startnode == "9":
        i=0
        j=2
    elif startnode == "10":
        i=2
        j=2
    elif startnode == "11":
        i=4
        j=2
    elif startnode == "12":
        i=6
        j=2
    elif startnode == "13":
        i=0
        j=0
    elif startnode == "14":
        i=2
        j=0
    elif startnode == "15":
        i=4
        j=0
    elif startnode == "16":
        i=6
        j=0

    for i in range(0,16):
        for j in range(0,16):
            distance = 0
            best = mn.konum[i][j]
            visited[i][j] = 1

            if(mn.konum[i][j] == 0):
                #---------------------------------------------------------------ortadaki düğümler için------------------
                if((mn.konum[i+1][j] < mn.konum[i-1][j]) and (mn.konum[i+1][j] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i+1][j]==0)):
                    distance += mn.konum[i+1][j]
                    visited[i+1][j] = 1
                    i+=1
                elif((mn.konum[i-1][j] < mn.konum[i+1][j]) and (mn.konum[i-1][j] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i-1][j]==0)):
                    distance += mn.konum[i-1][j]
                    visited[i-1][j] = 1
                    i-=1
                elif((mn.konum[i][j+1] < mn.konum[i][j-1]) and (mn.konum[i][j+1] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i][j+1]==0)):
                    distance += mn.konum[i][j+1]
                    visited[i][j+1] = 1
                    j+=1
                elif((mn.konum[i][j-1] < mn.konum[i][j+1]) and (mn.konum[i][j-1] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i][j-1]==0)):
                    distance += mn.konum[i][j-1]
                    visited[i][j-1] = 1
                    j-=1

                elif((mn.konum[i+1][j] < mn.konum[i][j-1]) and (mn.konum[i+1][j] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i+1][j]==0)):
                    distance += mn.konum[i+1][j]
                    visited[i+1][j] = 1
                    i+=1
                elif((mn.konum[i][j-1] < mn.konum[i+1][j]) and (mn.konum[i][j-1] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i][j-1]==0)):
                    distance += mn.konum[i][j-1]
                    visited[i][j-1] = 1
                    j-=1
                elif((mn.konum[i-1][j] < mn.konum[i][j-1]) and (mn.konum[i-1][j] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i-1][j]==0)):
                    distance += mn.konum[i-1][j]
                    visited[i-1][j] = 1
                    i-=1
                elif((mn.konum[i][j-1] < mn.konum[i-1][j]) and (mn.konum[i][j-1] < 13.0) and (i>0) and (i<7) and (j>0)and(j<7) and (visited[i][j-1]==0)):
                    distance += mn.konum[i][j-1]
                    visited[i][j-1] = 1
                    j-=1
                else:
                    break

parcacik()