def clean(p):
    res = {}
    for k in p:
        if p[k] != 0:
            res[k] = p[k]
    return res


def add(p1, p2):
    res = dict(p1)
    for k in p2:
        res[k] = res.get(k, 0) + p2[k]
    return clean(res)


def mul(p1, p2):
    res = {}
    for k1 in p1:
        for k2 in p2:
            k = k1 + k2
            res[k] = res.get(k, 0) + p1[k1] * p2[k2]
    return clean(res)


def print_poly(p):
    s = ""
    for k in sorted(p, reverse=True):
        c = p[k]
        if c == 0:
            continue
        if s == "":
            if c < 0:
                s = "-"
        elif c < 0:
            s += " - "
        else:
            s += " + "
        c = abs(c)
        if k == 0 or c != 1:
            s += str(c)
        if k == 1:
            s += "x"
        elif k > 1:
            s += "x^" + str(k)
    if s == "":
        s = "0"
    print(s)


def eval_poly(p, x):
    res = 0
    for k in p:
        res += p[k] * x ** k
    return res


p1 = {0: 7, 2: 1}
p2 = {1: 3, 2: -1}

print("p1:")
print_poly(p1)
print("p2:")
print_poly(p2)

print("сумма:")
print_poly(add(p1, p2))

print("произведение:")
print_poly(mul(p1, p2))

print("p1(2):", eval_poly(p1, 2))
