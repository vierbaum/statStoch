from math import comb
from fractions import Fraction as F

def bin(n, p, k):
    return comb(n, k) * p**k * (1-p)**(n-k)

for i in range(11):
    print(i, round(bin(10, 0.01, i), 3))
for i in range(10):
    print(i, round(bin(9, 0.01, i), 3))
