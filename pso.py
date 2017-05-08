import matrix_and_neo
import random as rand
import numpy as np
import matplotlib.pyplot as plt

def parcacik():
    #---------------------degiskenler ve ilk deger atamaları----------------------

    num_dimension = 2
    num_parcacik = 15

    p = np.empty((num_dimension, num_parcacik))
    v = np.empty((num_dimension, num_parcacik))

    pbest = np.empty((num_dimension, num_parcacik))
    gbest = np.empty((1,2))
    error = np.empty((num_parcacik))

    for i in range(0,num_dimension):
        for j in range(0,num_parcacik):
            pbest[i][j] = rand.randint(-7,7)
            p[i][j] = pbest[i][j]
            v[i][j] = 0

    #--------------anlik fitness fonksiyonunun hesaplanmasi-----------------------------------


    for i in range(0,num_parcacik):
        error[i] = fonksiyon(p[0][i], p[1][i])

    karsilastirma(pbest, error, num_parcacik)

    gbest[0][0] = pbest[0][0]
    gbest[0][1] = pbest[0][1]

    iterasyon = 0

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)

    while(iterasyon < 30):
        for i in range(0,num_parcacik):
            if (fonksiyon(p[0][i], p[1][i]))< (fonksiyon(pbest[0][i], pbest[1][i])):
                pbest[0][i] = p[0][i]
                pbest[1][i] = p[1][i]
            if (fonksiyon(pbest[0][i], pbest[1][i]))< (fonksiyon(gbest[0][0], gbest[0][1])):
                gbest[0][0] = p[0][i]
                gbest[0][1] = p[1][i]

            hiz_guncellemesi(num_parcacik, p, pbest, gbest, v)

            iterasyon +=1

            print ( "iterasyon: {} ---------- gbest:{} ".format(iterasyon, gbest))

            line1 = ax.plot(p[0],p[1],'error+')
            line2 = ax.plot(gbest[0][0], gbest[0][1], 'g*')

            ax.set_xlim(-3,3)
            ax.set_ylim(-3,3)

            fig.canvas.draw()

            ax.clear()
            ax.grid(True)

            print("gbest:{}".format(gbest))

def hiz_guncellemesi(num_parcacik, p, pbest, gbest, v):

    w = 0.7
    c1 = 1.47
    c2 = 1.47

    r1 = rand.random()
    r2 = rand.random()

    for i in range(0, num_parcacik):
        #--------- x ekseni icin hız guncellemesi
        v[0][i] = w*v[0][i] + c1*r1*(pbest[0][i]- p[0][i]) +c2**r1*(gbest[0][0]-p[0][i])
        p[0][i] = p[0][i] + v[0][i]
        # -------- y ekseni icin hız guncellemesi
        v[1][i] = w * v[1][i] + c1 * r1 * (pbest[1][i] - p[1][i]) + c2 ** r1 * (gbest[0][1] - p[1][i])
        p[1][i] = p[1][i] + v[1][i]

def fonksiyon(result_ym, result_dm):
    matrix_and_neo.result_yatay()
    matrix_and_neo.result_dikey()
    return result_ym + result_dm

def karsilastirma(pbest, error, num_parcacik):
    for i in range (1, num_parcacik):
        for j in range (0, num_parcacik-1):
            if (error[j] > error[j+1]):
                #fitness fonksiyonunu siralama
                temp = error[j]
                error[j] = error[j+1]
                error[j+1] =temp

                # en uygun pozisyonu siralama
                tempx = pbest[0][j]
                pbest[0][j] = pbest[0][j+1]
                pbest[0][j+1] = tempx

                tempy = pbest[1][j]
                pbest[1][j] = pbest[1][j + 1]
                pbest[1][j + 1] = tempy

if __name__== '__main__':
    parcacik()



