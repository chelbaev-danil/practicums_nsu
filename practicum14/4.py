n = int(input())

shapes = {}

for _ in range(n):
    parts = input().split()
    shape = parts[0]
    items = parts[1:]

    for item in items:
        shapes[item] = shape

item = input()
print(shapes[item])