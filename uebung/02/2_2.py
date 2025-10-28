from fractions import Fraction as F
from math import prod

p_a = F(3,15)
for a in (0, F(1,15)):
    for b in (0, F(2,15)):
        for c in (0, F(4, 15)):
            for d in (0, F(8, 15)):
                A = set((F(1,15), F(2,15)))
                B = set((a,b,c,d))
                if 0 in B:
                    B.remove(0)
                p_b = sum(B)
                p_ab = sum(A & B)
                if p_ab == p_a * p_b:
                    print(a,b,c,d)
