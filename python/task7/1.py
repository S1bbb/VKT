def normalize(p):
    while len(p) > 0 and p[-1] == 0:
        p.pop()
    return p


def add(p1, p2):
    res = [0] * max(len(p1), len(p2))
    for i in range(len(p1)):
        res[i] += p1[i]
    for i in range(len(p2)):
        res[i] += p2[i]
    return normalize(res)


def mul(p1, p2):
    if len(p1) == 0 or len(p2) == 0:
        return []
    res = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            res[i + j] += p1[i] * p2[j]
    return normalize(res)


def print_poly(p):
    s = ""
    for k in range(len(p) - 1, -1, -1):
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
    for k in range(len(p) - 1, -1, -1):
        res = res * x + p[k]
    return res


p1 = [7, 0, 1]
p2 = [0, 3, -1]

print("p1:")
print_poly(p1)
print("p2:")
print_poly(p2)

print("сумма:")
print_poly(add(p1, p2))

print("произведение:")
print_poly(mul(p1, p2))

print("p1(2):", eval_poly(p1, 2))
