def common_multiples(A: int, B: int, N: int):

    if A <= 0 or B <= 0 or N <= 0:
        print("A, B и N должны быть натуральными числами ")
        return
    
    found = False
    
    multiple = max(A, B)   
    
    while multiple <= N:
        if multiple % A == 0 and multiple % B == 0:
            print(multiple, end=' ')
            found = True
        multiple += 1
    
    if not found:
        print("Общих кратных не найдено.")
    else:
        print()  


input_A = int(input("Введите число A: "))   
input_B = int(input("Введите число B: "))
input_N = int(input("Введите число N: "))

common_multiples(input_A, input_B, input_N)