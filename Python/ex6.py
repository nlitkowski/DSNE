# Litkowski Norbert
# Cw.6
# Python

# Autoencoder

import math
import random

def f(x, beta):
    return 1/(1 + math.pow(math.e, (-1) * beta * x))

def get_sum_encoder(w, vec_x, b):
    sum = 0.0
    for j in range(25):
        sum += ((w[j] * vec_x[j]) + b)
    return sum

def get_sum_decoder(wp, vec_y, bp):
    sum = 0.0
    for i in range(16):
        sum += (wp[i] * vec_y[i]) + bp
    return sum

def get_e(vec_x, vec_xp):
    sum = 0.0
    for a in range(3):
        for k in range(25):
            sum += math.pow((vec_xp[a][k] - vec_x[a][k]), 2)
    return sum/2

def main():
    # inicjalizacja warunków początkowych
    beta = 1.0
    epsilon = 0.00001
    c = 0.8

    w = [[random.uniform(-0.5, 0.5) for j in range(16)] for i in range(25)]
    wp =[[random.uniform(-0.5, 0.5) for j in range(16)] for i in range(25)]
    
    b = [random.uniform(-0.5, 0.5) for i in range(16)]
    bp = [random.uniform(-0.5, 0.5) for i in range(25)]

    # inicjalizacja wektorów x
    x = []

    # a - położenia jedynek w wektorze
    a = [6, 7, 12, 17, 22]
    x.append([1.0 if i in a else 0.0 for i in range(25)])

    a = [2, 3, 8, 13]
    x.append([1.0 if i in a else 0.0 for i in range(25)])

    a = [5, 6, 11, 16, 21]
    x.append([1.0 if i in a else 0.0 for i in range(25)])

    # inicjalizacja wektorów y
    y = []

    for k in range(3):
        y.append([f(get_sum_encoder(w[i], x[k], b[i]), beta)
                  for i in range(16)])

    # inicjalizacja wektorów xp, xpp
    xp = []
    xpp = []

    for a in range(3):
        xp.append([])
        xpp.append([], [])
        for k in range(25):
            xp.append([f(get_sum_decoder(wp[k], y[a], bp[k]), beta)])
            f1 = lambda x: 0 if x < 0 else 1
            xpp[a].append(f1(xp[a][k]))

    # minimalizacja E metodą gradientu

if __name__ == "__main__":
    main()