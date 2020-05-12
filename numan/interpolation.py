from .util import *


def lagrangian(xx: str, yy: str, n: int = 0):
    '''Lagrangian interpolation.'''

    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

    if n == 0:
        n = len(xx)

    f = 0

    for i in range(n):
        f += factor(L(n, i, xx) * yy[i])

    return f, expand(f)


def newton(xx: str, yy: str, n: int = 0):
    '''Newton interpolation.'''

    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

    n = len(xx)

    f = 0

    for i in range(n):
        f += b(xx, yy, i)*p(xx, i)

    return f, expand(f)
