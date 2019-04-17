# Litkowski Norbert
# Cw.5
# Python

# Backpropagation

import math

def check_epsilon(s_new, s_old, w_new, w_old, eps):
    return max(abs(s_new - s_old), abs(w_new - w_old)) < eps      

def f(u, beta):
    return 1/(1 + math.e ** (-beta * u))

def f_prim(u, beta):
    val = f(u, beta)
    return beta * val * (1 - val)

def iterate(U, W, S, beta):
    x = [[] * 4]
    y = []
    Z = [0, 1, 1, 0]

    for p in range(4):
        x[p].extend(
            f(
                W[1][1] * U[p][1] +
                W[1][2] * U[p][2] +
                W[1][3] * U[p][3],
                beta
            ),
            f(
                W[2][1] * U[p][1] +
                W[2][2] * U[p][2] +
                W[2][3] * U[p][3],
                beta
            ),
            1
        )
        y.extend(
            f(
                S[1] * x[p][1] +
                S[2] * x[p][2] +
                S[3] * x[p][3],
                beta
            )
        )

def main():
    U = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    W = [
        [0, 1, 2],
        [0, 1, 2]
    ]
    S = [0, 1, 2]
    Beta = 1.0
    iterate(U, W, S, Beta)

if __name__ == "__main__":
    main()