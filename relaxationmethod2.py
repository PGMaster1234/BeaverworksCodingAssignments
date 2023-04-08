import math


def f(x):
    return math.tanh(5*x)


def relaxation_method2(func=None, xo=None, tol=None, max_it=None):
    output = [xo]
    c = 0
    tolerance = 64
    # print(xo)
    for i in range(max_it):
        if c < max_it:
            # print(xo)
            if c > 2:
                tolerance = math.fabs((pow((output[-1] - output[-2]), 2) / (2 * output[-2] - output[-3] - output[-1])))
            if tolerance < tol:
                return output
            if c + 1 < max_it:
                xo = func(xo)
                output.append(xo)
                c += 1

    return output


print(relaxation_method2(lambda x: 2 - math.exp(-x), xo=91.0, tol=1e-10, max_it=1))
