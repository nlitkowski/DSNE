# Litkowski Norbert
# Cw.4
# Python

# Gradient descent

import random


def check_epsilon(x_new, x_old, epsilon):
    sum = 0.0
    for i in range(len(x_new)):
        sum += abs(x_new[i] - x_old[i])
    if sum < epsilon:
        return False
    return True


def first_function(x, y, z):
    # x ** y => x to the power of y
    return 2 * x ** 2 + 2 * y ** 2 + z ** 2 - 2 * x * y - 2 * y * z - 2 * x + 3


def calculate_first_gradient(x_old, epsilon, c):
    print("First gradient")
    print(f"Values: [{x_old[0], x_old[1], x_old[2]}]")
    # function we are calculating gradient for
    print("f(x, y, z) = 2x^2 + 2y^2 + z^2 - 2xy - 2yz - 2x + 3\n")
    x_new = list(x_old)  # copy x_old to x_new
    flag = True
    while(flag):
        # assign x_old elements to variables for brevity
        x = x_old[0]
        y = x_old[1]
        z = x_old[2]
        x_new[0] = x - c * (4 * x - 2 * y - 2)
        x_new[1] = y - c * (4 * y - 2 * x - 2 * z)
        x_new[2] = z - c * (2 * z - 2 * y)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = list(x_new)  # copy x_new to x_old
    print(f"Point({x_new[0]}, {x_new[1]}, {x_new[2]})")
    print(f"Value: {first_function(x_new[0], x_new[1], x_new[2])}\n")


def second_function(x, y):
    # x ** y => x to the power of y
    return 3 * x ** 4 + 4 * x ** 3 - 12 * x ** 2 + 12 * y ** 2 - 24 * y


def calculate_second_gradient(x_old, epsilon, c):
    print("Second gradient")
    print(f"Values: [{x_old[0], x_old[1]}]")
    # function we are calculating gradient for
    print("f(x, y) = 3x^4 + 4x^3 - 12x^2 + 12y^2 - 24y\n")
    flag = True
    while(flag):
        # assign x_old elements to variables for brevity
        x = x_old[0]
        y = x_old[1]
        x_new = list(x_old)  # copy x_old to x_new
        x_new[0] = x - c * (12 * x ** 3 + 12 * x ** 2 - 24 * x)
        x_new[1] = y - c * (24 * y - 24)
        flag = check_epsilon(x_new, x_old, epsilon)
        x_old = list(x_new)  # copy x_new to x_old
    print(f"Point({x_new[0]}, {x_new[1]})")
    print(f"Value: {second_function(x_new[0], x_new[1])}\n")


def main():
    print("Gradient descent\n")
    # Predefine epsilon and c constant
    epsilon = 0.00001
    c = 0.01
    # Generate list of length 3 with random floats between -5 <= x < 5
    input_first = [round(random.uniform(-5, 5), 2) for i in range(3)]
    calculate_first_gradient(input_first, epsilon, c)
    # Generate list of length 2 with random floats between -3 <= x < 3
    input_second = [round(random.uniform(-3, 3), 2) for i in range(2)]
    calculate_second_gradient(input_second, epsilon, c)


if __name__ == "__main__":
    main()
