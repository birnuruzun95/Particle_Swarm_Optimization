# -*- coding: utf-8 -*-
import matrix_and_neo as mn
#import matplotlib.pyplot as plt

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
    global x
    global y
    matrix()
    best = []
    visited = [[0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0]]
    distance = 0
    startnode = int(input("Lütfen bulunduğunuz konumu ifade eden, 1-16 arasında bir konum  değeri giriniz:"))

    if(startnode == 1):
        x=0
        y=6
    elif(startnode == 2):
        x=2
        y=6
    elif(startnode == 3):
        x=4
        y=6
    elif(startnode == 4):
        x=6
        y=6
    elif(startnode == 5):
        x=0
        y=4
    elif(startnode == 6):
        x=2
        y=4
    elif(startnode == 7):
        x=4
        J=4
    elif(startnode == 8):
        x=6
        y=4
    elif(startnode == 9):
        x=0
        y=2
    elif(startnode == 10):
        x=2
        y=2
    elif(startnode == 11):
        x=4
        y=2
    elif(startnode == 12):
        x=6
        y=2
    elif(startnode == 13):
        x=0
        y=0
    elif(startnode == 14):
        x=2
        y=0
    elif(startnode == 15):
        x=4
        y=0
    elif(startnode == 16):
        x=6
        y=0

    for x in range(x,7):
        for y in range(y,7):
            if(mn.konum[x][y] == 0):
                best.append(startnode)
                visited[x][y] = 1
                #---------------------------------------------------------------ortadaki düğümler için------------------

                if(((x==0) or (x+1<7)) and ((y==0) or (y+1<7)) and (mn.konum[x+1][y] < 13.0)  and (visited[x+1][y]==0) and (mn.konum[x+1][y] < mn.konum[x-1][y])):
                    distance += (mn.konum[x+1][y])
                    best.append(startnode+1)
                    visited[x+1][y] = 1
                    x+=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x-1][y] < 13.0) and (visited[x-1][y]==0) and (mn.konum[x-1][y] < mn.konum[x+1][y])):
                    distance += mn.konum[x-1][y]
                    best.append(startnode-1)
                    visited[x-1][y] = 1
                    x-=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y+1] < 13.0) and (visited[x][y+1]==0) and (mn.konum[x][y+1] < mn.konum[x][y-1])):
                    distance += mn.konum[x][y+1]
                    best.append(startnode-4)
                    visited[x][y+1] = 1
                    y+=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y-1] < 13.0) and (visited[x][y-1]==0) and (mn.konum[x][y-1] < mn.konum[x][y+1])):
                    distance += mn.konum[x][y-1]
                    best.append(startnode+4)
                    visited[x][y-1] = 1
                    y-=1

#------------------------------------------------------------------------------------------------------------
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x+1][y] < 13.0) and (visited[x+1][y]==0) and (mn.konum[x+1][y] < mn.konum[x][y-1])):
                    distance += mn.konum[x+1][y]
                    best.append(startnode+1)
                    visited[x+1][y] = 1
                    x+=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y-1] < 13.0) and (visited[x][y-1]==0) and (mn.konum[x][y-1] < mn.konum[x+1][y])):
                    distance += mn.konum[x][y-1]
                    best.append(startnode+4)
                    visited[x][y-1] = 1
                    y-=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x+1][y] < 13.0) and (visited[x+1][y]==0) and (mn.konum[x+1][y] < mn.konum[x][y+1])):
                    distance += mn.konum[x+1][y]
                    best.append(startnode+1)
                    visited[x+1][y] = 1
                    x += 1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y+1] < 13.0) and (visited[x][y+1]==0) and (mn.konum[x][y+1] < mn.konum[x+1][y])):
                    distance += mn.konum[x][y+1]
                    best.append(startnode-4)
                    visited[x][y+1] = 1
                    y -= 1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x-1][y] < 13.0) and (visited[x-1][y]==0) and (mn.konum[x-1][y] < mn.konum[x][y-1])):
                    distance += mn.konum[x-1][y]
                    best.append(startnode-1)
                    visited[x-1][y] = 1
                    x-=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y-1] < 13.0) and (visited[x][y-1]==0) and (mn.konum[x][y-1] < mn.konum[x-1][y])):
                    distance += mn.konum[x][y-1]
                    best.append(startnode+4)
                    visited[x][y-1] = 1
                    y-=1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x-1][y] < 13.0) and (visited[x-1][y]==0) and (mn.konum[x-1][y] < mn.konum[x][y+1])):
                    distance += mn.konum[x-1][y]
                    best.append(startnode-1)
                    visited[x-1][y] = 1
                    x -= 1
                elif((x>0) and (x+1<7) and (y>0) and (y+1<7) and (mn.konum[x][y+1] < 13.0) and (visited[x][y+1]==0) and (mn.konum[x][y+1] < mn.konum[x-1][y])):
                    distance += mn.konum[x][y+1]
                    best.append(startnode-4)
                    visited[x][y+1] = 1
                    y -= 1
                else:
                    break

    print(best)
    print(distance)


parcacik()