# Litkowski Norbert
# Cw.2
# Python


def f(input, weight, m):
    x = 0.0
    for i in range(m):
        x += (weight[i] * input[i])
    if x >= 0:
        return 1
    else:
        return 0


def z(t):
    if ((t % 5) + 1) < 3:
        return 1.0
    else:
        return 0.0


def w(c, t, weights, inputs):
    zt = z(t)
    input = inputs[((t - 1) % 5)][len(weights) - 1]
    yt = y(weights, inputs, t)
    for i in range(len(weights)):
        weights[i] = (weights[i] + c * (zt - yt) * input)
    return weights


def iter(c, inputs):
    weights = list(range(26))
    weights[:] = [1.0] * 26

    t = 1
    counter = 0

    while(counter < 5):
        weights = w(c, t, weights, inputs)
        zt = z(t)
        yt = f(inputs[t % 5], weights, len(weights))
        for i in range(26):
            weights[i] = weights[i] + c * (zt - yt) * inputs[t % 5][i]
        t += 1
        if(zt == yt):
            counter += 1
        else:
            counter = 0
    print("\nC:{}\nT: {}\n".format(c,t))
    for i in range(len(weights)):
        print("W{}: {}".format(i, weights[i]))


def main():
    inputs = []
    tmp = list(range(26))

    # U1
    tmp[:] = [0.0] * 26
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[12] = 1.0
    tmp[17] = 1.0
    tmp[22] = 1.0
    tmp[25] = 1.0
    inputs.append(list(tmp[:]))

    # U2
    tmp[:] = [0.0] * 26
    tmp[2] = 1.0
    tmp[3] = 1.0
    tmp[8] = 1.0
    tmp[13] = 1.0
    tmp[25] = 1.0
    inputs.append(list(tmp[:]))

    # U3
    tmp[:] = [0.0] * 26
    tmp[5] = 1.0
    tmp[6] = 1.0
    tmp[11] = 1.0
    tmp[16] = 1.0
    tmp[21] = 1.0
    inputs.append(list(tmp[:]))

    # U4
    tmp[:] = [0.0] * 26
    tmp[6] = 1.0
    tmp[7] = 1.0
    tmp[8] = 1.0
    tmp[11] = 1.0
    tmp[13] = 1.0
    tmp[16] = 1.0
    tmp[17] = 1.0
    tmp[18] = 1.0
    tmp[25] = 1.0
    inputs.append(list(tmp[:]))

    # U5
    tmp[:] = [0.0] * 26
    tmp[10] = 1.0
    tmp[11] = 1.0
    tmp[12] = 1.0
    tmp[15] = 1.0
    tmp[17] = 1.0
    tmp[20] = 1.0
    tmp[21] = 1.0
    tmp[22] = 1.0
    tmp[25] = 1.0
    inputs.append(list(tmp[:]))

    for c in [0.01, 0.1, 1.0]:
        iter(c, inputs)


if __name__ == '__main__':
    main()
