from sympy import *
import matplotlib.pyplot as plt
import numpy as np

x, y = symbols('x y', real=True)


def show_roots(f, p):
    print(f'Actual root:')
    print(nsolve(f, p))


def plot_function(f, r):
    _x = np.linspace(r[0], r[1])
    _y = f(_x)

    plt.plot(_x, _y)


def bisection(f, a, b, n=5, t=10**-2):
    _p = a
    a = Rational(a)
    b = Rational(b)
    g = f.subs(x, y)

    for i in range(n):
        if f.subs(x, a)*g.subs(y, b) < 0:
            p = (a+b)/2
            print(f'x{i+1} = {p} = {N(p)}')

            if (b-a)/2 < t:
                break

            if f.subs(x, a)*g.subs(y, p) < 0:
                b = p
            elif f.subs(x, a)*g.subs(y, p) > 0:
                a = p
            else:
                break
        else:
            break

    print()
    show_roots(f, _p)


def newton(f, p0, n=10, t=10**-8, exact=False):
    _p = p0
    p0 = Rational(p0)
    f_ = diff(f, x)

    for i in range(n):
        if not exact:
            p = N(p0 - f.subs(x, p0)/f_.subs(x, p0))
            print(f'x{i+1} ~= {p}')
        else:
            p = p0 - f.subs(x, p0)/f_.subs(x, p0)
            print(f'x{i+1} = {p} ~= {N(p)}')

        if abs(p-p0) < t:
            break

        p0 = p

    print()
    show_roots(f, _p)


def secant(f, a, b, n=10, t=10**-8, exact=False):
    _p = a
    a = Rational(a)
    b = Rational(b)

    for i in range(n):
        if not exact:
            a, b = b, N(b - f.subs(x, b)*(b-a)/(f.subs(x, b) - f.subs(x, a)))
            print(f'x{i+2} ~= {b}')
        else:
            a, b = b, b - f.subs(x, b)*(b-a)/(f.subs(x, b) - f.subs(x, a))
            print(f'x{i+2} = {b} ~= {N(b)}')

        if abs((b-a)/b) < t:
            break

    print()
    show_roots(f, _p)
