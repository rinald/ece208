'''Defines a class for mathematical operations.'''

from .token import Token
from .errors import EvaluateError
from .util import OPERATORS, CONSTANTS

def _eval(node, _vars):
    if isinstance(node, Operation):
        value = node.eval(_vars)
    elif isinstance(node, str):
        if node in CONSTANTS:
            constant = node
            value = CONSTANTS[constant]
        else:
            variable = node
            
            if _vars == None:
                raise EvaluateError('Expressions can\'t have variables.')
            elif variable not in _vars:
                raise EvaluateError('Variable {} not initialised.'.format(variable))
            else:
                value = _vars[variable]
    else:
        value = node
        
    return value

class Operation:
    '''Defines a mathematical operation.'''

    def __init__(self, operator, left=None, right=None):  
        self.operator = operator
        self.left = left
        self.right = right

        if left != None and right != None:
            self.type = 'infix'
        elif left == None and right != None:
            self.type = 'prefix'
        elif left != None and right == None:
            self.type = 'postfix'
        else:
            self.type = 'undefined'

    def __str__(self):
        return '({}{}{})'.format(
            self.left if self.left is not None else '',
            self.operator,
            self.right if self.right is not None else ''
        )

    def __repr__(self):
        return self.__str__()

    def eval(self, _vars=None):
        '''Evaluate the operation.'''

        function = OPERATORS[self.type][self.operator]['function']

        if self.type == 'infix':
            left = _eval(self.left, _vars)
            right = _eval(self.right, _vars)

            return function(left, right)

        elif self.type == 'prefix':
            right = _eval(self.right, _vars)

            return function(right)

        elif self.type == 'postfix':
            left = _eval(self.left, _vars)

            return function(left)

        else:
            raise EvaluateError('Cannot evaluate operation of type {}.'.format(self.type))
