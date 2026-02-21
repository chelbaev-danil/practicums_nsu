string = input().lower()
for char in 'abcefghijklmnopqrstuvwxyz':
    if string.count(char) == 3:
        print(char)
        break