str = input()
max_count = 1
for char0 in range(0, len(str)):
    count = 1
    for char1 in range(char0 + 1, len(str)):
        if str[char0] == str[char1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
            break
print(max_count)