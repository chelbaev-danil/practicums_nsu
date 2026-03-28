def date_to_seconds(date_str: str) -> int:
    try:
        if ' ' not in date_str:
            raise ValueError("Неверный формат: отсутствует пробел между датой и временем")
        
        date_part, time_part = date_str.strip().split(' ', 1)
        month, day, year = map(int, date_part.split('/'))
        hour, minute, second = map(int, time_part.split(':'))
        
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть от 1 до 12")
        if not (1900 <= year <= 2100):
            raise ValueError("Год должен быть в диапазоне 1900–2100")
        if not (0 <= hour <= 23):
            raise ValueError("Часы должны быть от 0 до 23")
        if not (0 <= minute <= 59):
            raise ValueError("Минуты должны быть от 0 до 59")
        if not (0 <= second <= 59):
            raise ValueError("Секунды должны быть от 0 до 59")
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_month[1] = 29  # февраль в високосном году
        if not (1 <= day <= days_in_month[month - 1]):
            raise ValueError("Некорректная дата: неверное количество дней в месяце")
         
        seconds_in_current_day = hour * 3600 + minute * 60 + second
        days_passed = 0
        
        for m in range(1, month):
            days_passed += days_in_month[m - 1]
        
        days_passed += day - 1
        total_seconds = days_passed * 86400 + seconds_in_current_day
        
        return total_seconds
    
    except ValueError as e:
        print(f"Ошибка: {e}")
        return -1 
    except Exception:
        print("Ошибка: Неверный формат строки. Используйте 'MM/DD/YYYY HR:MIN:SEC'")
        return -1

print(date_to_seconds("01/01/2024 00:00:00"))   # 0
print(date_to_seconds("01/01/2024 00:00:01"))   # 1
print(date_to_seconds("01/02/2024 00:00:00"))   # 86400 (ровно сутки)
print(date_to_seconds("12/31/2024 23:59:59"))   # секунды за весь 2024 год
print(date_to_seconds("02/29/2024 12:30:45"))   # високосный год — должно работать
print(date_to_seconds("13/05/2024 10:00:00"))   # Ошибка: Месяц должен быть от 1 до 12
