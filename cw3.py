# Litkowski Norbert
# Cw.3
# Python


def sgn(M):
    for i in range(len(M)):
        if M[i] >= 0:
            M[i] = 1
        else:
            M[i] = -1
    return M


def F(W, U):
    M = list(range(25))
    for i in range(25):
        tmp = 0.0
        for j in range(25):
            tmp += W[i][j] * U[j]
        M[i] = tmp
    return M


def get_char(x):
    if x == -1:
        return ' '
    return '*'


def get_weights(z0, z1):
    weights = [[] for i in range(25)]
    for i in range(len(weights)):
        weights[i] = list(range(25))
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j] = ((1 / 25.0) * ((z0[i] * z0[j]) + (z1[i] * z1[j])))
    return weights


def get_char_matrix(Matrix):
    M = []
    for i in range(len(Matrix)):
        M.append(get_char(Matrix[i]))
    return M


def iterate(z0, z1, weights):
    Fnum0 = sgn(F(weights, z0))
    Fnum1 = sgn(F(weights, z1))
    F0 = get_char_matrix(Fnum0)
    F1 = get_char_matrix(Fnum1)
    print("Z0")
    for i in range(0, 21, 5):
        print(f"{F0[i]} {F0[i + 1]} {F0[i + 2]} {F0[i + 3]} {F0[i + 4]}")
    print("Z1")
    for i in range(0, 21, 5):
        print(f"{F1[i]} {F1[i + 1]} {F1[i + 2]} {F1[i + 3]} {F1[i + 4]}")


def main():
    print("Model asocjacji (Uczenie Hebba)\n")

    # inicjalizuję obrazy
    a = [6, 7, 8, 11, 13, 16, 17, 18]
    Z0 = [1 if i in a else -1 for i in range(25)]

    a = [6, 7, 12, 17]
    Z1 = [1 if i in a else -1 for i in range(25)]

    # inicjalizuję zaburzone obrazy
    a = [1, 2, 3, 6, 8, 11, 13, 16, 17, 18]
    ZP0 = [1 if i in a else -1 for i in range(25)]

    a = [2, 7, 12, 17, 22]
    ZP1 = [1 if i in a else -1 for i in range(25)]

    weights = get_weights(Z0, Z1)

    print("Normalne obrazy\n")
    iterate(Z0, Z1, weights)

    print("Zaburzone obrazy\n")
    iterate(ZP0, ZP1, weights)


if __name__ == "__main__":
    main()
