def print_special_numbers(A: int, B: int):

    if A > B:
        A, B = B, A
    
    allowed_digits = ['1', '3', '4', '8', '9']
    
    found = False
    
    for num in range(A, B + 1):
        
        str_num = str(num)
         
        if all(digit in allowed_digits for digit in str_num):
            print(num, end=' ')
            found = True
    
    if not found:
        print("В указанном диапазоне нет чисел с требуемыми цифрами.")
    else:
        print() 

print("Пример 1:")
print_special_numbers(1, 100)


