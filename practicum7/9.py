N, K, R = map(int, input().split())

days = 1

while N < R:
    N *= (1 + K / 100)
    days += 1
print(days)

