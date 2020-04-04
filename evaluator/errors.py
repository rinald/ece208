'''Defines errors.'''

class EvaluateError(Exception):
    '''Raised when the expression can't be evaluated.'''

    pass

class ParseError(Exception):
    '''Raised when a token can't be parsed.'''

    pass

class ReadError(Exception):
    '''Raised when the lexer doesn't know how to interpret a character.'''

    pass
