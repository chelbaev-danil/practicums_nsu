
with open("task7/input.txt", "r") as file:
    lines = file.readlines()

with open('task7/input.txt', "w", encoding="utf-8") as f:
    for line in lines:
        if "100" != line.strip():       
            f.write(line)
