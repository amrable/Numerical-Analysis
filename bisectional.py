# Python program for implementation
# of Bisection Method for
# solving equations

# Place your equation at this function.
# The function is x^3 - x^2 + 2
def func(x):
    return 3 * x * x * x * x + 6.1 * x * x * x - 2 * x * x + 3 * x + 2


# Prints root of func(x) and each iteration's state
# Parameters : left side, right side, tolerance and the equation defined as a function
def bisection(a, b, tolerance, function):
    if function(a) * function(b) >= 0:
        print("You have not assumed right a and b\n")
        return

    c = a
    i = 1;
    prev = 0;
    new = 0;
    print(
        "Iteration\t" + " Left\t\t\t" + " Right\t\t\t" + " Middle\t\t\t" + " f(Left)\t\t" + " f(Right)\t\t" + " f(Middle)\t\t" + " ea")

    while (b - a) >= tolerance:

        prev = c
        # Find middle point
        c = (a + b) / 2
        new = c
        funca = function(a)
        funcb = function(b)
        funcc = function(c)

        if i == 1 or new ==0:
            print("%d\t\t\t" % i, sci_notation(a, sig_fig=2), "\t", sci_notation(b, sig_fig=2), "\t",
                  sci_notation(c, sig_fig=2), "\t", sci_notation(funca, sig_fig=2), "\t",
                  sci_notation(funcb, sig_fig=2),
                  "\t", sci_notation(funcc, sig_fig=2), "\t")
        else:
            print("%d\t\t\t" % i, sci_notation(a, sig_fig=2), "\t", sci_notation(b, sig_fig=2), "\t",
                  sci_notation(c, sig_fig=2), "\t", sci_notation(funca, sig_fig=2), "\t",
                  sci_notation(funcb, sig_fig=2),
                  "\t", sci_notation(funcc, sig_fig=2), "\t", ((new - prev) / new) * 100)
        i = i + 1
        # Check if middle point is root
        if funcc == 0.0:
            break

        # Decide the side to repeat the steps
        if funcc * funca < 0:
            b = c
        else:
            a = c

        prev = c;

    print("The root is at : ", "%.8f" % c)


def sci_notation(number, sig_fig=2):
    ret_string = "{0:.{1:d}e}".format(number, sig_fig)
    a, b = ret_string.split("e")
    b = int(b)  # removed leading "+" and strips leading zeros too.
    return a + " * 10^" + str(b)


# Driver code
# Initial values assumed
a = -3

b = -1

es = 0.01


print("Bisection Method  [-1,-3]")
bisection(a, b, es, func)
