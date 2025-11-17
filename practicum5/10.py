a = int(input())

if 1000 <= a <= 9999:
    if not (1900 <= a <= 2050):
        if len(set(str(a))) == len(str(a)): 
            print("OK")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")