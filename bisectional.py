# Python program for implementation
# of Bisection Method for
# solving equations


# Place your equation at this function.
# The function is x^3 - x^2 + 2
def func(x):
    return x * x * x - 0.165 * x * x + 3.993 * 10 ** -4


# Prints root of func(x) and each iteration's state
# Parameters : left side, right side, tolerance and the equation defined as a function
def bisection(a, b, tolerance, function):
    if function(a) * function(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    i = 1;
    print(
        "Iteration\t" + " Left\t\t\t" + " Right\t\t\t" + " Middle\t\t\t" + " f(Left)\t\t\t" + " f(Right)\t\t\t" + " f(Middle)")

    while (b - a) >= tolerance:

        # Find middle point
        c = (a + b) / 2

        funca = function(a)
        funcb = function(b)
        funcc = function(c)

        print("%d\t\t\t" % i, sci_notation(a, sig_fig=3), "\t", sci_notation(b, sig_fig=3), "\t",
              sci_notation(c, sig_fig=3), "\t", sci_notation(funca, sig_fig=4), "\t", sci_notation(funcb, sig_fig=4),
              "\t", sci_notation(funcc, sig_fig=4), "\t")
        i = i + 1
        # Check if middle point is root
        if funcc == 0.0:
            break

        # Decide the side to repeat the steps
        if funcc * funca < 0:
            b = c
        else:
            a = c

    print("The root is at : ", "%.8f" % c)


def sci_notation(number, sig_fig=2):
    ret_string = "{0:.{1:d}e}".format(number, sig_fig)
    a, b = ret_string.split("e")
    b = int(b)  # removed leading "+" and strips leading zeros too.
    return a + " * 10^" + str(b)


# Driver code
# Initial values assumed
a = 0
b = 0.11
es = 0.0001
bisection(a, b, es, func)
