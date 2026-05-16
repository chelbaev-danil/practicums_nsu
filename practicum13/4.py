set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
target = int(input())

intersection = set1 & set2
print(target in intersection)