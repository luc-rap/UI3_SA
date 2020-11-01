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
    teplota = 300 # nastavit
    factor = 0.9995 # alfa faktor a.k.a. coolinf factor

    for i in range(1000):
        print(i, cena)
        teplota *= factor
        for j in range(400): # nastavit
            # vymen dve nahodne suradnice
            s1, s2 = numpy.random.randint(0, len(zoznam_miest), size=2)
            zoznam_miest[s1], zoznam_miest[s2] = zoznam_miest[s2], zoznam_miest[s1]
            cena_nova = vzdialenost_cesty(zoznam_miest)

            if cena_nova < cena:
                cena = cena_nova
            else:
                x = numpy.random.uniform() # " transition probability " - probability of transitioning from one state to another in a single step
                if x < numpy.exp((cena-cena_nova) / teplota): # pravdepdobnost ze prijme riesenie. cim je mensia teplota, s tym mensou p prijme nove riesenia
                    cena = cena_nova
                else: # ked neprijme riesenie, vratime naspat, skusame znovu
                    zoznam_miest[s1], zoznam_miest[s2] = zoznam_miest[s2], zoznam_miest[s1]

    return zoznam_miest


if __name__ == '__main__':
    #pocet_miest = 52
    zoznam_miest = []
    #generacie = 1000
    #fitness_celkovo = []
    with open('wi29.txt', 'r') as f:
        for row in f:
            x, y = row.strip().split()
            #zoznam_miest.append((int(x), int(y)))
            zoznam_miest.append((float(x), float(y)))
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