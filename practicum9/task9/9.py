
with open('task9/input.txt', 'r') as file:
    lines = file.readlines()

with open('task9/output.txt', 'w') as file:
    for line in lines[1::2]: 
        file.write(line + '')
