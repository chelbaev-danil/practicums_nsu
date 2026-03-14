with open('practicum9/task4/input.txt', 'r') as file:
    data = file.read().splitlines()

with open('practicum9/task4/output.txt', 'w') as file:
    for line in data:
        if len(line) > 20:
            file.write(line + '\n')