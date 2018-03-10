#https://www.codewars.com/kata/common-denominators/python
from decimal import Decimal
from functools import reduce


def gcd(a, b, *args):
    return gcd(b, a % b) if b != 0 else a


def lcd(lst):
    return reduce(lambda a, b: a/gcd(a, b) * b, lst)


def convertFracts(lst):
    denom = [d for n, d in lst]
    common = lcd(denom)
    return [[n*Decimal(common/d), common] for n, d in lst]

lst = [[27115, 5262], [87546, 11111111], [43216, 255689]]
expected = [
    [77033412951888085, 14949283383840498],
    [117787497858828,   14949283383840498],
    [2526695441399712,  14949283383840498]
]
assert convertFracts(lst) == expected
