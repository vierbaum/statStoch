from random import shuffle

def sim_sailors(n: int) -> int:
    sailors = list(range(n))
    shuffle(sailors)

    correct = 0
    for bed, sailor in enumerate(sailors):
        if bed == sailor:
            correct += 1

    return correct

num_simulations = 1000

print("x,y")
for n in range(1, 100):
    avg = 0
    for _ in range(num_simulations):
        avg += sim_sailors(n)
    print(f"{n},{avg/num_simulations}")
