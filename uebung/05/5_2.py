c = {"A": 10, "B": 8, "C": 10, "D": 16}

#b
#for f in ("A", "B", "C", "D"):
#    for s in sorted(set(["D", "C", "B", "A"]) - set([f])):
#        print(f"$({f},{s})$&$({c[f]},{c[s]})$&${int((c[f]+c[s])/2)}$\\\\")

#d
for f in ("A", "B", "C", "D"):
    for s in ("A", "B", "C", "D"):
        print(f"$({f},{s})$&$({c[f]},{c[s]})$&${int((c[f]+c[s])/2)}$\\\\")
