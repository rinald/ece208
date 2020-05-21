from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x, y = symbols('x y', real=True)


def show_roots(f, p):
    print(f'Actual root:')
    print(nsolve(f, p))


def plot_function(f, r):
    _x = np.linspace(r[0], r[1])
    _y = f(_x)

    plt.plot(_x, _y)


def L(n, i, xx):
    p = 1

    for j in range(n+1):
        if j == i:
            continue

        p *= (x-xx[j])/(xx[i]-xx[j])

    return p


def div_diff(xx, yy, i, j):
    if j-i == 1:
        return (yy[j] - yy[i])/(xx[j] - xx[i])
    else:
        return (div_diff(xx, yy, i+1, j) - div_diff(xx, yy, i, j-1))/(xx[j] - xx[i])


def b(xx, yy, i):
    if i == 0:
        return yy[0]
    else:
        return div_diff(xx, yy, 0, i)


def p(xx, i):
    _p = 1

    for j in range(i):
        _p *= (x-xx[j])

    return _p
