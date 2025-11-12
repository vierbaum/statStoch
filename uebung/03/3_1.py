from fractions import Fraction as F
from math import sqrt
prob = {
    (1, 1) : F(1, 6),
    (1, 2) : F(1, 6),
    (1, 3) : F(1, 6),
    (1, 4) : F(1, 6),
    (1, 5) : F(1, 6),
    (1, 6) : F(1, 6),
}

def get_prob(n, k):
    try:
        return prob[(n,k)]
    except Exception:
        return 0

def w(n, k):
    s = 0
    k_ = 0
    while k_ <= k:
        s += get_prob(n, k_)
        k_ += 1
    return s

def p(n, k):
    s = sum([get_prob(n-1, k - j) for j in (1,2,3,4,5,6)])
    prob[(n, k)] = s / 6

for n in range(2, 41):
    for k in range(n, 6 * n + 1):
        p(n, k)

def a():
    # dist
    string = "x,y\n"
    for k in range(5, 31):
        string += f"{k},{prob[5, k]:.10f}\n"
    with open("3_1dist.csv", "w") as f:
        f.write(string)

    # dist func
    dist_string = "x,y\n4,0\n"
    dist_points_string = "x,y\n"
    s = 0
    for k in range(5, 31):
        dist_string += f"{k},{s:.10f}\n\n"
        s += prob[5, k]
        dist_string += f"{k},{s:.10f}\n"
        dist_points_string += f"{k},{s:.10f}\n"
    dist_string += "31,1"

    with open("3_1distf.csv", "w") as f:
        f.write(dist_string)

    with open("3_1distfp.csv", "w") as f:
        f.write(dist_points_string)

def b():
    mu = F(7, 2)
    p = F(1, 6)
    epsilont_string = "x,y\n"
    epsilon_string = "x,y\n"
    sigma2 = F(35, 12)
    for n in range(2, 41):
        epsilon = sqrt(sigma2 / (n * p))
        epsilon_string += f"{n},{epsilon}\n"
        #epsilon_string += f"{n},{-epsilon}\n"
        kstar = 0
        while w(n, kstar) <= p / 2:
            kstar += 1
        epsilont = mu - kstar / n
        epsilont_string += f"{n},{epsilont}\n"

    with open("3_1epsilont.csv", "w") as f:
        f.write(epsilont_string)
    with open("3_1epsilon.csv", "w") as f:
        f.write(epsilon_string)

b()
