
def discount(price:int, card:bool, holidays:bool):
    total_discount = 0

    if price > 30000:
        total_discount += 0.1
    elif price > 20000:
        total_discount += 0.07
    elif price > 15000:
        total_discount += 0.05
    elif price > 5000:
        total_discount += 0.03
    
    if card:  
        total_discount += 0.05
    
    if holidays:
        total_discount += 0.03

    if total_discount > 0.15:
        total_discount = 0.15

    final_price = price * (1 - total_discount)

    return f'{final_price:.2f}'

input_price = int(input('Введите цену: '))
input_card = input('Есть ли у вас карта? (да/нет): ').lower()
input_holidays = input('Сегодня праздник? (да/нет): ').lower()

input_card = 'да' in input_card
input_holidays = 'да' in input_holidays

print(discount(input_price, input_card, input_holidays))