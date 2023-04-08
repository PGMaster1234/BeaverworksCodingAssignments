from math import tanh


def f(x):
    return tanh(5*x)


def relaxation_method1(func=None, xo=None, num_it=None):
    output = [xo]
    for i in range(num_it):
        output.append(func(xo))
        xo = func(xo)

    return output


print(relaxation_method1(func=f, xo=-0.5, num_it=5))
