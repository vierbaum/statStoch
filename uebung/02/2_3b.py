from fractions import Fraction as F
from math import prod

rolls_per_team = 5
p_hit = F(3,4)
p_miss = F(1,4)

# first n bits pos
first_team_mask = (1 << rolls_per_team) - 1
# next n bits pos
second_team_mask = first_team_mask << rolls_per_team

num_rolls = 2 << 2 * rolls_per_team - 1

# We use 0 as 0-diff index,
# 1 as 1-diff index,
# 2 * rolls_per_team + 1 as -1-diff index, etc.
hits = [[0, F(0, 1)] for _ in range(2 * rolls_per_team + 1)]

for shot in range(num_rolls):
    first_team_rolls = shot & first_team_mask
    second_team_rolls = shot & second_team_mask
    diff = first_team_rolls.bit_count() - second_team_rolls.bit_count()
    rolls_prob = [p_hit if (shot & 1 << i) else p_miss for i in range(2 * rolls_per_team)]
    shot_prob = prod(rolls_prob)
    hits[diff][0] += 1
    hits[diff][1] += shot_prob

for i in (-5,-4,-3,-2,-1,0,1,2,3,4,5):
    print(f"${i}$&${hits[i][0]}$&$\\frac{{{hits[i][1].numerator}}}{{{hits[i][1].denominator}}}$\\\\")
print([(hit[0], float(hit[1])) for hit in hits])
print(sum([hit[1] for hit in hits]))

print(bin(first_team_mask), bin(second_team_mask))
