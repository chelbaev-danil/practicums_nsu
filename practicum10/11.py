def is_prime(num: int) -> bool:

    if num <= 1:
        return False
    if num == 2:
        return True 
    if num % 2 == 0:
        return False 

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    
    return True

N = int(input("Введите натуральное число N: "))

for i in range(1, N + 1):
    if is_prime(i):
        print(i, end=' ')


