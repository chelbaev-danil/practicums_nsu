string = input().split()

for word in range(1, len(string)):
    if string[0] != string[word]:
        if len(set(string[word]))  == len(string[word]):
            print(string[word])
