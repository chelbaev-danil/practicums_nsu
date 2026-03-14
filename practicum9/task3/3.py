with open('task3/input.txt', 'r') as file:
    data = file.read().splitlines()

with open('task3/output.txt', 'w') as file:
    final_string = ''
    for line in data:
        final_string += line[0]
    file.write(final_string)