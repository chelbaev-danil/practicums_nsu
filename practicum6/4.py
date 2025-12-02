c = input("")
col_num = ord(c[0]) - ord('a') + 1
row_num = int(c[1])


if (col_num + row_num) % 2 == 0:
    print("черная")
else:
    print("белая")