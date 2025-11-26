from fractions import Fraction as F
s = set([1,2,3,4,5])
O = []
for _1 in s:
    for _2 in s - set([_1]):
        for _3 in s - set([_1, _2]):
            for _4 in s - set([_1, _2, _3]):
                for _5 in s - set([_1, _2, _3, _4]):
                    O.append((_1, _2, _3, _4, _5))

p = F(1, len(O))

def X(w):
    return w[0]

def Y(w):
    total = 0
    for expected, value in zip([1,2,3,4,5], w):
        if expected == value:
            total += 1
    return total

def XY(w):
    return X(w) * Y(w)

x_inv = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set()}
x_image = set()
for w in O:
    x_image.add(X(w))
    x_inv[X(w)].add(w)

y_inv = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set()}
y_image = set()
for w in O:
    y_image.add(Y(w))
    y_inv[Y(w)].add(w)

xy_inv = {k: set() for k in range(25 + 1)}
xy_image = set()
for w in O:
    xy_image.add(XY(w))
    xy_inv[XY(w)].add(w)

print(f"X(\\Omega)={x_image},Y(\\Omega)={y_image}")
print("&0&1&2&3&4&5\\\\\n\hline")
for x in (0,1,2,3,4,5):
    row = f"{x}"
    for y in (0,1,2,3,4,5):
        total = set()
        for x_ in range(x + 1):
            for y_ in range(y + 1):
                total = total.union(x_inv[x_].intersection(y_inv[y_]))

        row += "&$\\frac{%s}{%s}$"%(len(total), len(O))
    row += "\\\\"
    print(row)

E_x = 0
E_y = 0
E_xy = 0
for x in x_image:
    E_x += x * len(x_inv[x]) * p
for y in y_image:
    E_y += y * len(y_inv[y]) * p
for xy in xy_image:
    E_xy += xy * len(xy_inv[xy]) * p
print("\\E(X)=\\frac{%s}{%s},\\E(Y)=\\frac{%s}{%s},\\E(X\\cdot Y)=\\frac{%s}{%s}"%(
    E_x.numerator, E_x.denominator,
    E_y.numerator, E_y.denominator,
    E_xy.numerator, E_xy.denominator,
))
