n = int(input())
c = int(input())
num = int(input())

rec_per_page = n*c
page = (num-1)//(rec_per_page) + 1
pos_on_page = (num-1)%rec_per_page
row = pos_on_page // c + 1
col = pos_on_page % c + 1
print(f"страница {page} столбец {col} строка {row}")
