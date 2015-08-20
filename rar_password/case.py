import itertools


def make_cases(integer, lower, upper, special, min, max):
    chars = []
    if integer:
        chars += [str(x) for x in range(0, 10)]
    if lower:
        chars += [chr(x) for x in range(ord('a'), ord('z')+1)]
    if upper:
        chars += [chr(x) for x in range(ord('A'), ord('Z')+1)]
    if special:
        chars += [
            '`',
            '~',
            '!',
            '@',
            '#',
            '$',
            '%',
            '^',
            '&',
            '*',
            '(',
            ')',
            '-',
            '_',
            '=',
            '+',
            '[',
            '{',
            ']',
            '}',
            '\\',
            '|',
            ';',
            ':',
            '\'',
            '"',
            ',',
            '<',
            '.',
            '>',
            '/',
            '?',
        ]
    return itertools.chain.from_iterable([itertools.combinations_with_replacement(chars, n) for n in range(min, max+1)])
