# Litkowski Norbert
# Cw.1
# Python

# McCulloch-Pitts neuron


def f(weights, inputs, m):
    x = float(0)
    for i in range(m):
        x += (weights[i] * inputs[i])
    if x >= 0:
        return 1
    else:
        return 0


def and_gate():
    inputs = []
    weights = [float(0.3), float(0.3), float(-0.5)]
    m = 3
    print('\nAND gate\n')
    x = input('Input 1: ')
    y = input('Input 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nBad input')
        return
    print("\nResult: {}".format(f(weights, inputs, m)))


def nand_gate():
    inputs = []
    weights = [float(-0.4), float(-0.4), float(0.6)]
    m = 3
    print('\nNAND gate\n')
    x = input('Input 1: ')
    y = input('Input 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nBad input')
        return
    print("\nResult: {}".format(f(weights, inputs, m)))


def or_gate():
    inputs = []
    weights = [float(0.3), float(0.3), float(-0.2)]
    m = 3
    print('\nOR gate\n')
    x = input('Input 1: ')
    y = input('Input 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nBad input')
        return
    print("\nResult: {}".format(f(weights, inputs, m)))


def not_gate():
    inputs = []
    weights = [float(-0.5), float(0.3)]
    m = 2
    print('\nNOT gate\n')
    x = input('Input: ')
    if(x.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(1))
    else:
        print('\nBad input')
        return
    print("\nResult: {}".format(f(weights, inputs, m)))


def main():
    while True:
        print("\n1. NOT gate")
        print("2. AND gate")
        print("3. NAND gate")
        print("4. OR gate")
        print("0. Exit")
        x = input("\nChoice: ")
        try:
            x = int(x)
        except ValueError:
            print("\nBad input")
        if(x == 1):
            not_gate()
        elif(x == 2):
            and_gate()
        elif(x == 3):
            nand_gate()
        elif(x == 4):
            or_gate()
        elif(x == 0):
            break
        else:
            print("\nBad input...")


if __name__ == '__main__':
    main()
