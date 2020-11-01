import random
import matplotlib.pyplot as plt
import math
import numpy


def vzdialenost(mesto_1, mesto_2):
    d = math.sqrt((mesto_1[0] - mesto_2[0])**2 + (mesto_1[1]-mesto_2[1])**2)
    return d

# vypocita celkovu vzdialenost celej cesty //
def vzdialenost_cesty(cesta):
    dlzka_cesty = 0
    for i in range(0, len(cesta)):
        mesto_1 = cesta[i] # z ktoreho mesta ideme
        if i == len(cesta) - 1: # posledne mesto sa vracia do prveho
            mesto_2 = cesta[0]
            dlzka_cesty += vzdialenost(mesto_1, mesto_2)
        else:
            mesto_2 = cesta[i + 1] # nasledujuce mesto
            dlzka_cesty += vzdialenost(mesto_1, mesto_2)
    return dlzka_cesty

def simulovane_zihanie(zoznam_miest):
    cena = vzdialenost_cesty(zoznam_miest)
    #print(cena)
    teplota = 30
    factor = 0.9995 # alfa faktor
    t_initial = teplota

    for i in range(1500):
        print(i, cena)
        teplota *= factor
        for j in range(50):
            # vymen dve nahodne suradnice
            s1, s2 = numpy.random.randint(0, len(zoznam_miest), size=2)
            zoznam_miest[s1], zoznam_miest[s2] = zoznam_miest[s2], zoznam_miest[s1]
            cena_nova = vzdialenost_cesty(zoznam_miest)

            if cena_nova < cena:
                cena = cena_nova
            else:
                x = numpy.random.uniform()
                if x < numpy.exp((cena-cena_nova) / teplota): # pravdepdobnost ze prijme riesenie
                    cena = cena_nova
                else:
                    zoznam_miest[s1], zoznam_miest[s2] = zoznam_miest[s2], zoznam_miest[s1]

    return zoznam_miest


if __name__ == '__main__':
    pocet_miest = 20
    zoznam_miest = []
    generacie = 1000
    fitness_celkovo = []
    #with open('berlin52.txt', 'r') as f:
        #for row in f:
           # x, y = row.strip().split()
            #zoznam_miest.append((int(x), int(y)))
    #print(zoznam_miest)

    # for i in range(0, pocet_miest):
    # x = int(random.random() * 200)
    # y = int(random.random() * 200)
     #zoznam_miest.append((x, y))
    zoznam_miest.append((60, 200))
    zoznam_miest.append((180, 200))
    zoznam_miest.append((100, 180))
    zoznam_miest.append((140, 180))
    zoznam_miest.append((20, 160))
    zoznam_miest.append((80 ,160))
    zoznam_miest.append((200 ,160))
    zoznam_miest.append((140 ,140))
    zoznam_miest.append((40 ,120))
    zoznam_miest.append((120 ,120))
    zoznam_miest.append((180 ,100))
    zoznam_miest.append((60 ,80))
    zoznam_miest.append((100 ,80))
    zoznam_miest.append((180 ,60))
    zoznam_miest.append((20 ,40))
    zoznam_miest.append((100 ,40))
    zoznam_miest.append((200 ,40))
    zoznam_miest.append((20 ,20))
    zoznam_miest.append((60 ,20))
    zoznam_miest.append((160 ,20))


    #populacia = vytvor_populaciu(zoznam_miest, 100)
    #print(zoznam_miest)

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    for first, second in zip(zoznam_miest[:-1], zoznam_miest[1:]):
        ax1.plot([first[0], second[0]] , [first[1], second[1]], 'b')
    ax1.plot([zoznam_miest[0][0], zoznam_miest[-1][0]], [zoznam_miest[0][1], zoznam_miest[-1][1]], 'b')
    for c in zoznam_miest:
        ax1.plot(c[0], c[1], 'ro')

    zoznam_miest = simulovane_zihanie(zoznam_miest)
    #simulovane_zihanie(zoznam_miest)
    for first, second in zip(zoznam_miest[:-1], zoznam_miest[1:]):
        ax2.plot([first[0], second[0]] , [first[1], second[1]], 'b')
    ax2.plot([zoznam_miest[0][0], zoznam_miest[-1][0]], [zoznam_miest[0][1], zoznam_miest[-1][1]], 'b')
    for c in zoznam_miest:
        ax2.plot(c[0], c[1], 'ro')

    plt.show()