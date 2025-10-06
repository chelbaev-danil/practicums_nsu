x, y = map(int, input().split())
res = (x%y==0) + (y%x==0)
print(res)