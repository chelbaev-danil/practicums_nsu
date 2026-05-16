from itertools import permutations

elements = sorted(input().split())

for p in permutations(elements):
    print(" ".join(p))