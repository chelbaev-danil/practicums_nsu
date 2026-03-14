from datetime import datetime

with open("task10/input.txt", "r") as f:
    data = f.read().splitlines()

today_day, today_month = data[0].split(".")
today_date = datetime(datetime.now().year, int(today_month), int(today_day))

with open("task10/output.txt", "w") as f:
    for line in data[2:]:

        cell, date = line.split()
        cell_day, cell_month = date.split(".")
        cell_date = datetime(
            datetime.now().year, 
            int(cell_month), 
            int(cell_day)
        )
        delta = (today_date - cell_date).days

        if delta > 3:
            f.write(f"{cell}\n")

