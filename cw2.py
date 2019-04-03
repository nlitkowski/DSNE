# Litkowski Norbert
# Cw.2
# Python

# Perceptron


def f(input, weight, m):
    x = 0.0
    for i in range(m):
        x += (weight[i] * input[i])
    if x >= 0:
        return 1
    else:
        return 0


def z(t):
    if (t % 5 + 1) <= 3:
        return 1.0
    else:
        return 0.0


def iter(c, inputs):
    weights = list(range(26))
    weights[:] = [1.0] * 26

    t = 1
    counter = 0.0

    while(counter < 5.0):
        zt = z(t)
        yt = f(inputs[t % 5], weights, len(weights))
        for i in range(26):
            weights[i] = weights[i] + c * (zt - yt) * inputs[t % 5][i]
        t += 1
        if(zt == yt):
            counter += 1.0
        else:
            counter = 0.0
    print("\nC:{}\nT: {}\n".format(c, t))
    for i in range(len(weights)):
        print("W{}: {}".format(i, weights[i]))


def main():
    inputs = []

    # U1
    a = [6, 7, 12, 17, 22, 25]
    inputs.append([1.0 if i in a else 0.0 for i in range(26)])

    # U2
    a = [2, 3, 8, 13, 25]
    inputs.append([1.0 if i in a else 0.0 for i in range(26)])

    # U3
    a = [5, 6, 11, 16, 21]
    inputs.append([1.0 if i in a else 0.0 for i in range(26)])

    # U4
    a = [6, 7, 8, 11, 13, 16, 17, 18, 25]
    inputs.append([1.0 if i in a else 0.0 for i in range(26)])

    # U5
    a = [10, 11, 12, 15, 17, 20, 21, 22, 25]
    inputs.append([1.0 if i in a else 0.0 for i in range(26)])

    # invoke iteration for different learning factors
    for c in [0.01, 0.1, 1.0]:
        iter(c, inputs)


if __name__ == '__main__':
    main()
