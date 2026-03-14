with open('task2/input.txt', 'r') as file:
    data = file.read().splitlines()

with open('task2/output.txt', 'w') as file:
    for line in data:
        if line[0].lower() == 'a':
            file.write(line + '\n')