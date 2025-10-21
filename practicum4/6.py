score = input("Введите счет (формат: число:число): ")

t1, t2 = map(int, score.split(':'))

if t1 > t2:
    print(1)
elif t2> t1:
    print(2)
else:
    print(0)