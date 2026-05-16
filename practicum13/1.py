numbers = list(map(int, input().split()))
target = int(input())

duplicates = set()
seen = set()

for n in numbers:
    if n in seen:
        duplicates.add(n)
    seen.add(n)

print(target in duplicates)