'''Defines the Expression object.'''

from .parser import Parser
from .operation import _eval

class Expression:
    '''Defines an expression.'''

    def __init__(self, expression):
        self.expression = expression
        self.ast = Parser(expression).parse()

    def __str__(self):
        return '<expression \'{}\'>'.format(self.expression)

    def __repr__(self):
        return self.__str__()
    
    def eval(self):
        '''Evaluate the expression.'''

        return _eval(self.ast, _vars=None)