cities = input().lower().split()

for num_city in range(len(cities)-1):
    if cities[num_city][-1] != cities[num_city+1][0]:
        print("Петя" if num_city % 2 == 0 else "Вася")
        break
else:
    print("Вася" if len(cities) % 2 == 0 else "Петя")

    