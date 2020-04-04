'''Defines the Function object.'''

from .parser import Parser
from .operation import _eval

class Function:
    '''Defines a function.'''

    def __init__(self, expression):
        parser = Parser(expression)
        self.expression = expression
        self.vars = parser.vars
        self.ast = parser.parse()

    def __str__(self):
        return '<function \'{}\'>'.format(self.expression)

    def __repr__(self):
        return self.__str__()

    def eval(self, *args, **kwargs):
        '''Evaluate the function.'''

        for i in range(min(len(args), len(self.vars))):
            kwargs[self.vars[i]] = args[i]

        return _eval(self.ast, _vars=kwargs)

    def __call__(self, *args, **kwargs):
        return self.eval(*args, **kwargs)
