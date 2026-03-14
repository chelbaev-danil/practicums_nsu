
with open ('task1/input.txt', 'r') as file:
    data = file.read().splitlines()

with open('task1/output.txt', 'w') as file:
    for line in data:
        file.write(f"{line.upper()}\n")
