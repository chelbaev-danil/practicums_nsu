N = float(input())

hours = N // 30
minutes = (N % 30) * 2

print(int(hours), int(minutes))