c = 0
k = float(input())
while True:
    b = float(input())
    if b == 0:  
        break
    if k > b:
        c += 1
    k = b
print(c)