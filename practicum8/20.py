def number_to_words(n):
    
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", 
             "семнадцать", "восемнадцать", "девятнадцать"
            ]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    thousands = ["", "тысяча", "тысячи", "тысяч"]

    def get_thousands_form(number):
        if 11 <= number % 100 <= 19:
            return thousands[3]
        elif number % 10 == 1:
            return thousands[1]
        elif 2 <= number % 10 <= 4:
            return thousands[2]
        else:
            return thousands[3]

    def three_digit_to_words(num, is_thousands=False):

        result = []
        result.append(hundreds[num // 100])  
        if 10 <= num % 100 <= 19: 
            result.append(teens[num % 100 - 10])
        else:
            result.append(tens[(num % 100) // 10]) 
            if is_thousands and num % 10 in [1, 2]:  
                result.append(["", "одна", "две"][num % 10])
            else:
                result.append(ones[num % 10])  
        return " ".join(filter(None, result))

    
    millions = n // 1_000_000
    thousands_part = (n // 1_000) % 1_000
    remainder = n % 1_000

    words = []
    if millions > 0:
        words.append(three_digit_to_words(millions))
        words.append("миллион" if millions == 1 else "миллиона" if 2 <= millions % 10 <= 4 else "миллионов")
    if thousands_part > 0:
        words.append(three_digit_to_words(thousands_part, is_thousands=True))
        words.append(get_thousands_form(thousands_part))
    if remainder > 0:
        words.append(three_digit_to_words(remainder))

    return " ".join(words)


number = int(input())
if 1 <= number <= 900_000_000:
    print(number_to_words(number))
else:
    print("Число вне допустимого диапазона.")