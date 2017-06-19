# -*- coding: utf-8 -*-
import matrix_and_neo as mn
import matplotlib.pyplot as plt

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
pbest = []
gbest = []
listx = []
listy = []
def bul(x,y):
    global visited
    global pbest
    global distance
    global listx
    global listy

    if ((x == 6) and (y == 0)):
        mn.matris_yazdir(visited)
        print("\n")
        distance=0
        for i in range(0, 7):
            for j in range(0, 7):
                if (visited[i][j] == 1):
                    distance += (mn.konum[i][j])
                    listx.insert(i, i)
                    listx.insert(j, j)
                else:
                    distance += 0
        pbest.append(distance)
        print(distance)
        print("\n")

        """if (gbest == distance):
            plt.ion()
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.grid(True)
            plt.hold(True)
            line = ax.plot(listx, listy, label="en kısa yol")

            ax.step(listx, listy)
            ax.legend()
            ax.set_xlim(0, 7)
            ax.set_ylim(0, 7)

            fig.canvas.draw()
            ax.clear()
            ax.grid(True)
            plt.show(block=True)"""
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
    global pbest
    global gbest

    matrix()

    startnode = int(input("Lütfen bulunduğunuz konumu ifade eden, 1-16 arasında bir konum  değeri giriniz:\n"))

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
    for i in range(0, len(pbest) - 1):  # buradaki parçacık sayısı 8
        if (pbest[i] > pbest[i + 1]):
            temp = pbest[i]
            pbest[i] = pbest[i + 1]
            pbest[i + 1] = temp
    gbest = pbest[0]
    # pbest[i] ye ait olan visited değerini çizdirsin
    print("gbest: {}".format(gbest))
    print("pbest: {}".format(pbest))




parcacik()