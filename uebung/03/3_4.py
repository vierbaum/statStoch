import numpy as np

def fx(x):
    l = 1 / 2
    return l * np.exp(-l * x)
def F(x):
    l = 1 / 2
    return 1 - np.exp(-l * x)

fx_string = "x,y\n-1,0\n0,0\n\n"
for x in np.linspace(0, 8, 100):
    fx_string += f"{x},{fx(x)}\n"

with open("3_4fx.csv", "w") as f:
    f.write(fx_string)

F_string = "x,y\n-1,0\n"
for x in np.linspace(0, 8, 100):
    F_string += f"{x},{F(x)}\n"

with open("3_4F.csv", "w") as f:
    f.write(F_string)
