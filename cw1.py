#Litkowski Norbert
#Cw.1
#Python

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
    weights = [float(0.3),float(0.3),float(-0.5)]
    m = 3
    print('\nBramka AND\n')
    x = input('Podaj wejście 1: ')
    y = input('Podaj wejście 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nZłe wejście')
        return
    print("\nWynik: {}".format(f(weights,inputs,m)))


def nand_gate():
    inputs = []
    weights = [float(-0.4),float(-0.4),float(0.6)]
    m = 3
    print('\nBramka NAND\n')
    x = input('Podaj wejście 1: ')
    y = input('Podaj wejście 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nZłe wejście')
        return
    print("\nWynik: {}".format(f(weights,inputs,m)))


def or_gate():
    inputs = []
    weights = [float(0.3),float(0.3),float(-0.2)]
    m = 3
    print('\nBramka OR\n')
    x = input('Podaj wejście 1: ')
    y = input('Podaj wejście 2: ')
    if(x.isdigit() and y.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(int(y)))
        inputs.append(float(1))
    else:
        print('\nZłe wejście')
        return
    print("\nWynik: {}".format(f(weights,inputs,m)))


def not_gate():
    inputs = []
    weights = [float(-0.5),float(0.3)]
    m = 2
    print('\nBramka NOT\n')
    x = input('Podaj wejście: ')
    if(x.isdigit()):
        inputs.append(float(int(x)))
        inputs.append(float(1))
    else:
        print('\nZłe wejście')
        return
    print("\nWynik: {}".format(f(weights,inputs,m)))


def main():
    while True:
        print("\n1. Bramka NOT")
        print("2. Bramka AND")
        print("3. Bramka NAND")
        print("4. Bramka OR")
        print("0. Wyjście")
        x = input("\nWybór: ")
        try:
            x = int(x)
        except ValueError:
            print("Złe wejście")
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
            print("\nZłe wejście...")


if __name__ == '__main__':
    main()
