position = int(input())
if position == 1:
    result_digit = 0
else:
    current_position = 1
    result_digit = None
    for number in range(1, 201):
        for digit in str(number):
            current_position += 1
            if current_position == position:
                result_digit = int(digit)
                break
        if result_digit is not None:
            break
print(result_digit)