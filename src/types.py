PRECEDENCE = { '+': 1, '-': 1, '*': 2, '/': 2, }
RIGHT_ASSOCIATIVE = set()

PRECEDENCE_REGEX = {
    '|': 1,
    '.': 2,
    '*': 3,
    '+': 3,
    '?': 3
}

REGEX_UNARY_OPERATORS = {'*', '+', '?'}
RIGHT_ASSOCIATIVE_REGEX = set()

#_OPERATOR_DESCRIPTION = {
#    '.': "Concatenation with",
#    '|': "Union with",
#    '*': "Kleene of",
#}