lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

start = int(input())
end = int(input())

segment = lst1[start-1:end][::-1]

lst2.extend(segment)

del lst1[start-1:end]

print(lst1)
print(lst2)