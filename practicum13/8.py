nums = input().split()
subsets = {frozenset()} 

for x in nums:
    new_subsets = {s | {x} for s in subsets}
    subsets |= new_subsets

print([list(s) for s in subsets])