x1,x2=map(int, input().split("x"))
a,b,c = map(int, input().split("x"))

s = x1*x2
if s >= a*b or s >= a*c or s >= b*c:
    print("Да")
else:
    print("Нет")