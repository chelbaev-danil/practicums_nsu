import math

while True:
    n = int(input())
    r = math.isqrt(n)
    if r * r == n:
        print(f"Число {n} является полным квадратом.")
        break
    else:
        print(f"Число {n} не является полным квадратом. Попробуйте снова.")


