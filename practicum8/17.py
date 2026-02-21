def evaluate_expression(expression):
    def calculate(ops, nums):
        
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        if op == '+':
            nums.append(a + b)
        elif op == '-':
            nums.append(a - b)
        elif op == '*':
            nums.append(a * b)
        elif op == '/':
            nums.append(a / b)

    def precedence(op):
       
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    nums = []  # Стек для чисел
    ops = []   # Стек для операторов
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            nums.append(num)
            i -= 1  
        elif char == '(':
            ops.append(char)
        elif char == ')':
            
            while ops and ops[-1] != '(':
                calculate(ops, nums)
            ops.pop() 
        elif char in '+-*/':
            
            while ops and precedence(ops[-1]) >= precedence(char):
                calculate(ops, nums)
            ops.append(char)
        i += 1

    
    while ops:
        calculate(ops, nums)

    return nums[0]

expression = input()
result = evaluate_expression(expression)
print(result)