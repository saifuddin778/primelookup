import sys
sys.dont_write_bytecode = True
import math

candidates = ['a',
                     'b',
                     'c',
                     'd',
                     'e',
                     'f',
                     'g',
                     'h',
                     'i',
                     'j',
                     'k',
                     'l',
                     'm',
                     'n',
                     'o',
                     'p',
                     'q',
                     'r',
                     's',
                     't',
                     'u',
                     'v',
                     'w',
                     'x',
                     'y',
                      'z',
                      '0',
                      '1',
                     '2',
                     '3',
                     '4',
                     '5',
                     '6',
                     '7',
                     '8',
                     '9',
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
                      '+',
                      '=',
                      '[',
                      ']',
                      '{',
                      '}',
                      '\\',
                      '/',
                      ':',
                      '.',
                      ',',
                      '<',
                      '>',
                      '?',
                      '|']

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gen_4n3():
    k = []
    n = 1000
    for a in range(1, n):
        pc = is_prime(((4*a) + 3))
        if pc:
            k.append(((4*a) + 3))
            if len(k) == 65:
                break
    return dict([(val, prime) for val, prime in zip(candidates, k)])

