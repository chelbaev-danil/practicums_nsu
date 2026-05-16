from itertools import permutations

for p in permutations(range(10), 6):
    x, o, d, m, a, t = p
    
    if x == 0 or m == 0:
        continue
        
    xod = x * 100 + o * 10 + d
    mat = m * 100 + a * 10 + t
    
    if xod + xod + xod == mat:
        print(f"{xod}+{xod}+{xod}={mat}")