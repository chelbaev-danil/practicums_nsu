n = int(input())

galleons = n // (17 * 29)
n %= (17*29)

sickles = n // 29
n %= 29

if galleons > 0:
    print(f"{galleons} галлеонов")
if sickles > 0:
    print(f"{sickles} сиклей")
if n > 0:
    print(f"{n} кнатов")
