
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(a)
n = int(input('Введите число: '))
fibonacci(n)