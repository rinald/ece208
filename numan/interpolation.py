from .util import *


def _convert(x):
    if isinstance(x, (int, float, str)):
        return Rational(str(x))
    else:
        return x


def lagrangian(xx: str, yy: str, n: int = -1):
    '''Lagrangian interpolation.'''

    xx = list(map(Rational, xx.split()))
    yy = list(map(Rational, yy.split()))

    assert len(xx) == len(yy)

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

    if n == 0:
        n = len(xx)
    else:
        n += 1

    f = 0

    for i in range(n):
        f += b(xx, yy, i)*p(xx, i)

    return f, collect(expand(f), x)
