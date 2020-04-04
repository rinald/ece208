'''Defines utility functions and structures.'''

import numpy as np
MAX_BP = 5


def is_digit(ch):
    return ch != '' and ch in '0123456789'


def is_letter(ch):
    return ch != '' and ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_operator(ch):
    return ch != '' and ch in '+-*/#^%!`'


def is_bracket(ch):
    return ch != '' and ch in '()[]{}<>'


def is_whitespace(ch):
    return ch != '' and ch in ' \n\t'


CONSTANTS = {
    'e': np.e,
    'pi': np.pi,
    'i': 1j,
    'phi': (1 + np.sqrt(5)) / 2
}

OPERATORS = {
    'infix':
    {
        '+': {
            'bp': 1,
            'function': lambda x, y: x+y
        },
        '-': {
            'bp': 1,
            'function': lambda x, y: x-y
        },
        '*': {
            'bp': 2,
            'function': lambda x, y: x*y
        },
        '/': {
            'bp': 2,
            'function': lambda x, y: x/y
        },
        '#': {
            'bp': 2,
            'function': lambda x, y: x % y
        },
        '^': {
            'bp': 3,
            'function': lambda x, y: x**y
        },
    },
    'prefix':
    {
        '+': {
            'bp': 4,
            'function': lambda x: x
        },
        '-': {
            'bp': 4,
            'function': lambda x: -x
        },
        'abs': {
            'bp': 4,
            'function': lambda x: abs(x)
        },
        'sqrt': {
            'bp': 4,
            'function': lambda x: np.sqrt(x)
        },
        'floor': {
            'bp': 4,
            'function': lambda x: np.floor(x)
        },
        'ceil': {
            'bp': 4,
            'function': lambda x: np.ceil(x)
        },
        'sin': {
            'bp': 4,
            'function': lambda x: np.sin(x)
        },
        'cos': {
            'bp': 4,
            'function': lambda x: np.cos(x)
        },
        'tan': {
            'bp': 4,
            'function': lambda x: np.tan(x)
        },
        'exp': {
            'bp': 4,
            'function': lambda x: np.exp(x)
        },
        'ln': {
            'bp': 4,
            'function': lambda x: np.log(x)
        },
        'log': {
            'bp': 4,
            'function': lambda x: np.log10(x)
        }
    },
    'postfix':
    {
        '!': {
            'bp': 5,
            'function': lambda x: np.math.factorial(x)
        },
        '%': {
            'bp': 5,
            'function': lambda x: x/100
        },
        '`': {
            'bp': 5,
            'function': lambda x: (x*np.pi)/180
        }
    }
}
