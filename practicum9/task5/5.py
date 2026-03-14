try:

    with open('task5/input.txt', 'r') as f:
        a, b, c = map(int, f.read().split())
    
    result = a / b + c
    
    with open('task5/output.txt', 'w') as f:
        f.write(str(result))

except ValueError:
    with open ('task5/output.txt', 'w') as f:
        f.write("data error")
except ZeroDivisionError:
    with open ('task5/output.txt', 'w') as f:
        f.write("division by 0")