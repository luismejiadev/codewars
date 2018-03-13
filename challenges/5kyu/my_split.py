#https://www.codewars.com/kata/55e0467217adf9c3690000f9

import re


def my_very_own_split(string, delimiter=None):
    if delimiter == "":
        raise ValueError("empty separator")
    elif delimiter is None:
        step = 1
        get_index = lambda x: re.search("\s+", x).start() if re.search("\s+", x) else -1
    else:
        step = len(delimiter)
        get_index = lambda x: x.find(delimiter)
    index = get_index(string)
    while index >= 0:
        sub = string[:index]
        if sub or delimiter:
            yield sub
        string = string[index+step:]
        index = get_index(string)
    yield string

