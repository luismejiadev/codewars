#https://www.codewars.com/kata/last-digit-of-a-huge-number/train/python

from functools import reduce


def get_expo(n):
    if n <= 4: return n
    tail = n % 100 if n % 100 > 1 else n % 1000
    expo = 4 if tail % 4 == 0 else tail % 4
    result = expo if expo > 1 else tail
    return result


def last_digit(numbers):
    if not numbers: return 1
    if len(numbers) == 1: return numbers[0] % 10
    expo = numbers[1] if len(numbers) == 2 else reduce(lambda y, x: x ** get_expo(y), numbers[1:][::-1])
    return ((numbers[0] % 10) ** get_expo(expo)) % 10

test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6),
    ([2147483647, 343], 3),
    ([2147483647, 2147483647, 2147483647, 2147483647], 3),
    ([2, 2, 101, 2], 6),
    ([0, 9999], 0)
]
for n, e in test_data:
    print "iniciando", n
    r = last_digit(n)
    print r, e
    assert r == e
