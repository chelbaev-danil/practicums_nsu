def get_card_value():

    try:
        price = float(input("Введите стоимость телефонной карты ($): "))
    except ValueError:
        print("Ошибка: Введите числовое значение!")
        return None
    
    if price == 5 or price == 10:
        bonus = 0
    elif price == 25:
        bonus = 3
    elif price == 50:
        bonus = 8
    elif price == 100:
        bonus = 20
    else:
        print("Допускаются только карты стоимостью $5, $10, $25, $50 или $100.")
        return None
    
    total_value = price + bonus
    
    print(f"Карта стоимостью ${price} с бонусом даёт ${total_value} времени.")
    return total_value


get_card_value()