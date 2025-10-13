from random import randint
import numpy as np

def sim_collection(n: int) -> list[int]:
    collection: list[bool] = [False for _ in range(n)]
    next: list[int] = []

    current_turn = 1
    while not all(collection):
        card: int = randint(0, n - 1)
        if not collection[card]:
            collection[card] = True
            next.append(current_turn)

        current_turn += 1

    return next

n = 100
num_simulations = 1000
next = np.array([0 for _ in range(n)])

for _ in range(num_simulations):
    next += np.array(sim_collection(n))

print(sum(next / num_simulations))
