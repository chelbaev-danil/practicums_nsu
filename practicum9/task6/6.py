try:

    with open("task6/input.txt", "r") as file:
        data = file.read().splitlines()

    line_numbers = data[0]
    lines_count = 0

    for line in data[1:]:
            lines_count += 1

    if lines_count != int(line_numbers):
        with open("task6/output.txt", "w") as file:
            file.write("NO")    
    else: 
        with open("task6/output.txt", "w") as file:
            file.write("YES")

except ValueError:
    with open("task6/output.txt", "w") as file:
        file.write("error")

