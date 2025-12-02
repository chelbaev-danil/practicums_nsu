k = int(input())

def order(k):
    for x in range(k // 5 + 1):
        if (k - 5 * x) % 7 == 0:
            return True
    return False

if order(k):
    print("Можно заказать")
else:
    print("Нельзя заказать")
