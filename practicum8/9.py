string = input().split(" ")
for WordNumber in range(len(string)-1):
    if string[WordNumber] == string[WordNumber+1]:
        print(string[WordNumber])
        break
