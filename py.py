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

visited = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]


def bul(x, y):
    global  visited


    if ((x == 6) and (y == 0)):
        mn.matris_yazdir(visited)
        print("\n\n")
       # visited[x][y] = 0
        return x,y
    if ((x+1 < 7) and (visited[x+1][y] == 0) and (mn.konum[x+1][y]<13.0) and (mn.konum[x+1][y] != 2)):
        visited[x+1][y] = 1
        bul(x+1, y)
        visited[x+1][y] = 0
    if ((y+1 < 7) and (visited[x][y+1] == 0) and (mn.konum[x][y+1]<13.0) and (mn.konum[x][y+1] != 2)):
        visited[x][y+1] = 1
        bul(x, y+1)
        visited[x][y+1] = 0
    if ((x-1 >= 0) and (visited[x-1][y] == 0) and (mn.konum[x-1][y]<13.0) and (mn.konum[x-1][y] != 2)):
        visited[x-1][y] = 1
        bul(x-1, y)
        visited[x-1][y] = 0
    if ((y-1 >= 0) and (visited[x][y-1] == 0) and (mn.konum[x][y-1]<13.0) and (mn.konum[x][y-1] != 2)):
        visited[x][y-1] = 1
        bul(x, y-1)
        visited[x][y-1] = 0



def parcacik():
    global x
    global y

    matrix()
    best = []

    distance = 0

    startnode = int(input("Lütfen bulunduğunuz konumu ifade eden, 1-16 arasında bir konum  değeri giriniz:"))

    if(startnode == 1):
        x=6
        y=0
    elif(startnode == 2):
        x=6
        y=2
    elif(startnode == 3):
        x=6
        y=4
    elif(startnode == 4):
        x=6
        y=6
    elif(startnode == 5):
        x=4
        y=0
    elif(startnode == 6):
        x=4
        y=2
    elif(startnode == 7):
        x=4
        y=4
    elif(startnode == 8):
        x=4
        y=6
    elif(startnode == 9):
        x=2
        y=0
    elif(startnode == 10):
        x=2
        y=2
    elif(startnode == 11):
        x=2
        y=4
    elif(startnode == 12):
        x=2
        y=6
    elif(startnode == 13):
        x=0
        y=0
    elif(startnode == 14):
        x=0
        y=2
    elif(startnode == 15):
        x=0
        y=4
    elif(startnode == 16):
        x=0
        y=6

    for x in range(x,7):
        for y in range(y,7):
            visited[x][y] = 0
            if(mn.konum[x][y] == 0):
                visited[x][y] = 1
                bul(x,y)
                break
        break


parcacik()