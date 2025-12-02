n = int(input())
m = int(input())
k = int(input("число кварталов "))
possible = False
for i in range(1, n):
    if i * m == k:
        possible = True
        break
if not possible:
    for j in range(1, m):
        if j * n == k:
            possible = True
            break

print("да" if possible else "нет")
