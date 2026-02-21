string1 = input().lower()
string2 = input().lower()
string3 = input().lower()
for char in string1:
    if char not in string2 and char not in string3:
        print(char, end=' ')
        break
for char in string2:
    if char not in string1 and char not in string3:
        print(char, end=' ')
        break
    
for char in string3:
    if char not in string2 and char not in string1:
        print(char, end=' ')
        break

