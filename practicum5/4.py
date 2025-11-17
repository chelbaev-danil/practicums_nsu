num = int(input())
ld = num % 10

if 11 <= num % 100 <= 19:
    print(f"{num} попугаев") 
elif ld == 1:
    print(f"{num} попугай") 
elif 2 <= ld <= 4:
    print(f"{num} попугая") 
else:
    print(f"{num} попугаев") 

