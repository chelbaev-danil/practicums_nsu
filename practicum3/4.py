x, y, n = map(int, input().split())

rub = x*n + (y*n)//100
kop = (y*n)%100

print(f"{rub} руб. {kop} коп.")