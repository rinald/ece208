from .util import *


def _convert(x):
    if isinstance(x, (int, float, str)):
        return Rational(str(x))
    else:
        return x


def lagrangian(xx: list, yy: list, n: int = -1):
    '''Lagrangian interpolation.'''

    assert len(xx) == len(yy)

    xx = list(map(_convert, xx))
    yy = list(map(_convert, yy))

    if n == -1:
        n = len(xx)-1

    f = 0

    for i in range(n+1):
        f += factor(L(n, i, xx) * yy[i])

    return f, collect(expand(f), x)


def newton(xx: str, yy: str, n: int = 0):
    '''Newton interpolation.'''

    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

    n = len(xx)

    f = 0

    for i in range(n):
        f += b(xx, yy, i)*p(xx, i)

    return f, collect(expand(f), x)
