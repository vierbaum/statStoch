import math

def po(k, l):
    return math.e ** (-l) * l**k / math.factorial(k)

print((po(1, 1) * 1/4 + po(1, 10) * 3/4) * 100)
print((po(0, 10) * 3/4) / (po(0, 1) * 1/4 + po(0, 10) * 3/4)*100)
print((po(0, 10)/(po(0,1) + po(0, 10)))*100)
