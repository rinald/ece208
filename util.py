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


def bisection(f, a, b, n=5, t=10**-2):
    _p = a
    root = nsolve(f, a)

    _ex = [a, b]
    _x = [a, b]
    _e = ['', '']

    a = Rational(a)
    b = Rational(b)
    g = f.subs(x, y)

    for _ in range(n):
        if f.subs(x, a)*g.subs(y, b) < 0:
            p = (a+b)/2
            _ex.append(p)
            _x.append(N(p))
            _e.append(f'{N(abs(b-a)/2):.15f}')

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

    _x.append(root)
    _e.append(f'{0.0:.15f}')
    _ex.append('')

    df = pd.DataFrame({
        'x (exact)': _ex,
        'x': _x,
        'error': _e,
    })

    df = df.rename(index={len(df)-1: 'root'})

    return df


def newton(f, p0, n=10, t=10**-8, exact=False):
    _p = p0
    f_ = diff(f)
    root = nsolve(f, p0)

    _x = [p0]
    _e = ['']

    if exact:
        _ex = [p0]

    p0 = Rational(p0)

    for _ in range(n):
        if exact:
            p = p0 - f.subs(x, p0)/f_.subs(x, p0)
            _ex.append(p)
            _x.append(N(p))
        else:
            p = N(p0 - f.subs(x, p0)/f_.subs(x, p0))
            _x.append(p)

        _e.append(f'{N(abs(p-p0)):.15f}')

        if abs(p-p0) < t:
            break

        p0 = p

    _x.append(root)
    _e.append(f'{0.0:.15f}')

    if exact:
        _ex.append('')
        d = {'x (exact)': _ex}
    else:
        d = {}

    df = pd.DataFrame({
        **d,
        'x': _x,
        'error (%)': _e,
    })

    df = df.rename(index={len(df)-1: 'root'})

    return df


def secant(f, a, b, n=10, t=10**-8, exact=False):
    _p = a
    root = nsolve(f, a)

    _x = [a, b]
    _e = ['', '']

    if exact:
        _ex = [a, b]

    a = Rational(a)
    b = Rational(b)

    for _ in range(n):
        if exact:
            a, b = b, b - f.subs(x, b)*(b-a)/(f.subs(x, b) - f.subs(x, a))
            _ex.append(b)
            _x.append(N(b))
        else:
            a, b = b, N(b - f.subs(x, b)*(b-a)/(f.subs(x, b) - f.subs(x, a)))
            _x.append(b)

        _e.append(f'{N(abs(b-a)):.15f}')

        if abs(b-a) < t:
            break

    _x.append(root)
    _e.append(f'{0.0:.15f}')

    if exact:
        _ex.append('')
        d = {'x (exact)': _ex}
    else:
        d = {}

    df = pd.DataFrame({
        **d,
        'x': _x,
        'error (%)': _e,
    })

    df = df.rename(index={len(df)-1: 'root'})

    return df


def L(n, i, xx):
    p = 1

    for j in range(n):
        if j == i:
            continue

        p *= (x-xx[j])/(xx[i]-xx[j])

    return p


def interpolation(xx, yy, n=0):
    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

    if n == 0:
        n = len(xx)

    f = 0

    for i in range(n):
        f += factor(L(n, i, xx) * yy[i])

    return f, expand(f)


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


def newton_interpolation(xx, yy):
    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

    n = len(xx)

    f = 0

    for i in range(n):
        f += b(xx, yy, i)*p(xx, i)

    return f, expand(f)
