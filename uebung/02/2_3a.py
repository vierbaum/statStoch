from math import comb
from fractions import Fraction as F

def binomial(p, n, k):
    return comb(n, k) * p**k * (1-p)**(n-k)

for k in (0,1,2,3,4):
    print(k, binomial(F(1,2), 3, k), binomial(F(3,4), 2, k))
