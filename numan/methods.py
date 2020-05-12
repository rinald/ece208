from .util import *


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


def gauss_seidel(a, b, n=10, exact=False):
    assert (m := len(a)) == len(a[0]) == len(b)

    _x = [Rational(0)] * m
    _y = []

    for _ in range(n):
        for i in range(m):
            s = 0

            for j in range(m):
                if j != i:
                    s += a[i][j]*_x[j]
            if not exact:
                _y.append(N((b[i] - s) / a[i][i]))
            else:
                _y.append((b[i] - s) / a[i][i])

        _x = _y
        _y = []

        print(_x)
