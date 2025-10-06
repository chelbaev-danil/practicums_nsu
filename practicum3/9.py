ATT=int(input()) # количество попыток паса (attempts)
COMP=int(input()) # количество завершенных пасов (completions)
YDS=int(input()) # ярды, набранные пасом (yards)
TD=int(input()) # количество тачдаунов (touchdowns)
INT=int(input()) # количество перехватов (interceptions)
a = ((COMP / ATT) - 0.3) * 5 # 1. Процент завершенных пасов
b = ((YDS / ATT) - 3) * 0.25 # 2. Ярды за попытку
c = (TD / ATT) * 20  # 3. Процент тачдаунов
d = 2.375 - ((INT / ATT) * 25) # 4. Процент перехватов
result = ((a + b + c + d) / 6) * 100 #Расчет итогового рейтинга
print(result)