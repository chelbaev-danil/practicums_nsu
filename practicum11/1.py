numbers = list(map(int, input().split()))

new_list = []
for i in range(8):
    new_list.append(numbers[i] + numbers[i+1])

print(new_list)

