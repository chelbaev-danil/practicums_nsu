nums = input().split()
k = int(input())
subsets = {frozenset()}

for x in nums:
    subsets |= {s | {x} for s in subsets if len(s) < k}

result = [list(s) for s in subsets if len(s) == k]
print(result)