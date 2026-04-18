lst = list(map(int, input().split()))

command = input().strip()

direction = command[0]
steps = int(command[1:]) 

if direction == 'R':
    steps = steps % len(lst)
    lst = lst[-steps:] + lst[:-steps]
elif direction == 'L':
    steps = steps % len(lst)
    lst = lst[steps:] + lst[:steps]

print(lst)