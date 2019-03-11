# Litkowski Norbert
# Cw.2
# Python


def f(inputs, weights):
    x = float(0)
    for i in range(min(len(inputs), len(weights))):
        x += (weights[i] * inputs[i])
    if x >= 0:
        return 1
    else:
        return 0


def learn


def main():
    inputs = [[0, 0, 0, 0, 0,
               0, 1, 1, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 1, 0, 0, 1],
              [0, 0, 1, 1, 0,
               0, 0, 0, 1, 0,
               0, 0, 0, 1, 0,
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0,
               1, 1, 0, 0, 0,
               0, 1, 0, 0, 0,
               0, 1, 0, 0, 0,
               0, 1, 0, 0, 0, 1],
              [0, 0, 0, 0, 0,
               0, 1, 1, 1, 0,
               0, 1, 0, 1, 0,
               0, 1, 1, 1, 0,
               0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               1, 1, 1, 0, 0,
               1, 0, 1, 0, 0,
               1, 1, 1, 0, 0, 1]]
    for c in [0.01, 0.1, 1.0]:
        print("")


if __name__ == '__main__':
    main()
