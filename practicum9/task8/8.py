days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("task8/input.txt", encoding="utf-8") as f:
    steps = [int(line.strip()) for line in f]

if len(steps) == 366:
    days_in_month[1] = 29

start = 0
averages = []

for days in days_in_month:
    month_steps = sum(steps[start : start + days])
    avg = month_steps / days
    averages.append(avg)
    start += days

with open("task8/output.txt", "w", encoding="utf-8") as f:
    for avg in averages:
        f.write(f"{int(avg)}\n")