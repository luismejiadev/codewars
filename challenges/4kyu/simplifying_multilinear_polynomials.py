import re
def defactor(value):
    r = re.split('(\d+)', value)
    if len(r) > 1:
        return int(r[1]), r[2]
    else:
        return 1, r[0]

def refactor(final):
    output = []
    for k in sorted(final.keys(), key=lambda x: (len(x), x)):
        v = final[k]
        if v == -1:
            output.append("-")
            output.append(k)
        elif v <0:
            output.extend([str(v),k])
        elif v == 1:
            if output:
                output.append("+")
            output.append(k)
        elif v > 1:
            if output:
                output.append("+")
            output.extend([str(v), k])
    return "".join(output)

def simplify(poly):
    result2 = []
    for r in poly.split("+"):
        values = r.split("-")
        if values[0]:
            value = values[0]
            result2.append(defactor(value))
        for e in values[1:]:
            if e:
                value = e
                n, v = defactor(value)
                result2.append((-n, v))
    final = {}
    for n, v in result2:
        v = "".join(sorted(v))
        final[v] = final.get(v, 0) + n
    return refactor(final)