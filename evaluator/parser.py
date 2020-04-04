'''Defines the parser to be used by Expression and Function.'''

from .lexer import Lexer
from .errors import ParseError
from .operation import Operation
from .util import OPERATORS, CONSTANTS, MAX_BP

class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.lexer = Lexer(expression)
        self.depth = 0
        self.vars = []

    def bp(self, token):
        '''Return the binding power of a token.'''

        if token == None:
            return -1
        if token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['postfix']:
                return self.depth * MAX_BP + OPERATORS['postfix'][operator]['bp']
            else:
                return self.depth * MAX_BP + OPERATORS['infix'][operator]['bp']
        elif token.type == 'function':
            function = token.value
            return self.depth * MAX_BP + OPERATORS['prefix'][function]['bp']
        elif token.value in [')', ']', '}', '>']:
            self.lexer.next()
            self.depth -= 1
            return -1
        else:
            return -1

    def nud(self, token):
        '''Parse a token with no left context.'''

        parse = self.parse
        bp = self.bp

        if token.type == 'integer':
            return int(token.value)
        elif token.type == 'float':
            return float(token.value)
        elif token.type == 'constant':
            return token.value
        elif token.type == 'variable':
            variable = token.value
            if variable not in self.vars:
                self.vars.append(variable)
            return variable
        elif token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['prefix']:
                _bp = self.depth * MAX_BP + OPERATORS['prefix'][operator]['bp']
                return Operation(operator, right=parse(rbp=_bp))
            else:
                raise ParseError('\'{}\' is not a prefix operator.'.format(operator))
        elif token.type == 'function':
            function = token.value
            return Operation(function, right=parse(rbp=bp(token)))
        elif token.value == '(':
            self.depth += 1
            return parse(rbp=self.depth*MAX_BP)
        elif token.value == '[':
            self.depth += 1
            return Operation('floor', right=parse(rbp=self.depth*MAX_BP))
        elif token.value == '{':
            self.depth += 1
            return Operation('ceil', right=parse(rbp=self.depth*MAX_BP))
        elif token.value == '<':
            self.depth += 1
            return Operation('abs', right=parse(rbp=self.depth*MAX_BP))
        else:
            raise ParseError('Cannot parse {}'.format(token))

    def led(self, left, token):
        '''Parse a token with a left context.'''

        parse = self.parse
        bp = self.bp

        if token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['postfix']:
                return Operation(operator, left=left)
            else:
                if operator == '^':
                    return Operation(operator, left=left, right=parse(rbp=bp(token)-1))
                else:
                    return Operation(operator, left=left, right=parse(rbp=bp(token)))
        else:
            return None

    def parse(self, rbp=0):
        '''Parse an expression with the "Top Down Operator Parsing" algorithm.'''

        # Aliases
        lexer = self.lexer
        nud = self.nud
        led = self.led
        bp = self.bp

        # The actual algorithm
        left = nud(lexer.next())

        while bp(lexer.peek()) > rbp:
            left = led(left, lexer.next())

        return left
