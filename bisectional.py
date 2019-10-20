# Python program for implementation
# of Bisection Method for
# solving equations


# Place your equation at this function.
# The function is x^3 - x^2 + 2
def func(x):
    return x * x - 3


# Prints root of func(x)
# with error of EPSILON
def bisection(a, b, tolerance):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    i = 1;
    print("Iteration\t" + "Left\t\t" + "Right\t\t" + "Middle\t\t" + "f(Left)\t\t" + "f(Right)\t" + "f(Middle)")

    while (b - a) >= tolerance:

        # Find middle point
        c = (a + b) / 2

        funca = func(a)
        funcb = func(b)
        funcc = func(c)

        # Check if middle point is root
        if funcc == 0.0:
            break

        # Decide the side to repeat the steps
        if funcc * funca < 0:
            b = c
        else:
            a = c

        print("%d\t\t\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t" % (i, a, b, c, funca, funcb, funcc))
        i = i + 1

    print("The root is at : ", "%.8f" % c)


# Driver code
# Initial values assumed
a = 1
b = 2
es = 0.01
bisection(a, b, es)
