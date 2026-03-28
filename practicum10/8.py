def convert_date_time(date_str: str):
    
    try:
        if ' ' not in date_str:
            print("Ошибка: Неверный формат. Должно быть 'MM/DD/YYYY HR:MIN:SEC'")
            return
        
        date_part, time_part = date_str.strip().split(' ', 1)
        
        if '/' not in date_part:
            print("Ошибка: Неверный формат даты. Используйте MM/DD/YYYY")
            return
        
        month, day, year = date_part.split('/')
        
        if ':' not in time_part:
            print("Ошибка: Неверный формат времени. Используйте HR:MIN:SEC")
            return
        
        hour, minute, second = time_part.split(':')
        
        month = int(month)
        day = int(day)
        year = int(year)
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        
        if not (1 <= month <= 12):
            print("Ошибка: Месяц должен быть от 1 до 12")
            return
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_month[1] = 29  # високосный год
        
        if not (1 <= day <= days_in_month[month-1]):
            print("Ошибка: Некорректное количество дней в месяце")
            return
        
        if not (1900 <= year <= 2100):  
            print("Ошибка: Год должен быть между 1900 и 2100")
            return
        
        if not (0 <= hour <= 23):
            print("Ошибка: Часы должны быть от 0 до 23")
            return
        if not (0 <= minute <= 59):
            print("Ошибка: Минуты должны быть от 0 до 59")
            return
        if not (0 <= second <= 59):
            print("Ошибка: Секунды должны быть от 0 до 59")
            return
        
        dd = f"{day:02d}"
        mm = f"{month:02d}"
        yy = f"{year % 100:02d}"
        
        if hour == 0:
            hour12 = 12
            period = "AM"
        elif hour < 12:
            hour12 = hour
            period = "AM"
        elif hour == 12:
            hour12 = 12
            period = "PM"
        else:
            hour12 = hour - 12
            period = "PM"
        
        print(f"{dd}.{mm}.{yy} {hour12:02d}:{minute:02d}:{second:02d} {period}")
        
    except ValueError:
        print("Ошибка: Неверный формат ввода. Используйте 'MM/DD/YYYY HR:MIN:SEC'")
    except Exception as e:
        print(f"Ошибка: {e}")



convert_date_time("12/04/1990 13:12:12")   # 04.12.90 01:12:12 PM
convert_date_time("02/29/2024 00:00:00")   # 29.02.24 12:00:00 AM
