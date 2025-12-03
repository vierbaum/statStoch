import scipy
import numpy as np

n = 10
percentiles = {}
for i in range(1, 11):
    pi = (i - 1/2) / n
    percentiles[i] = scipy.stats.norm(loc=0, scale=1).ppf(pi)
percentiles[n + 1] = percentiles[n] + 0.5
print(percentiles)

f_str = f"x,y\n -4,0\n{percentiles[1]},0"
marks_str = "x,y\n"
for x in range(1, n + 1):
    f_str += f"\n\n{percentiles[x]},{x / 10}\n{percentiles[x+1]},{x/10}"
    marks_str += f"{percentiles[x]},{x / 10}\n"
f_str += "\n4,1"
with open("4_1X.csv", "w") as f:
    f.write(f_str)
with open("4_1Xm.csv", "w") as f:
    f.write(marks_str)

f_str = f"x,y\n"
for x in np.arange(-4, 4, 0.05):
    f_str += f"{x},{scipy.stats.norm(loc=0, scale=1).cdf(x)}\n"
with open("4_1Y.csv", "w") as f:
    f.write(f_str)
