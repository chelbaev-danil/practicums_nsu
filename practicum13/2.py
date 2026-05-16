n = int(input())
all_unique = set()

for _ in range(n):
    student_courses = set(input().split())
    all_unique |= student_courses

print(len(all_unique))