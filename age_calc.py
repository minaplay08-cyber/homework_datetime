"""
Задача 1: Калькулятор возраста
"""
from datetime import date, datetime


def calculate_age():
    print("=" * 50)
    print("КАЛЬКУЛЯТОР ВОЗРАСТА")
    print("=" * 50)
    
    while True:
        birth_date_str = input("Введите дату рождения (ДД.ММ.ГГГГ): ").strip()
        try:
            birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
            break
        except ValueError:
            print("Ошибка: введите дату в формате ДД.ММ.ГГГГ")
    
    today = date.today()
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        days += 30
    
    if months < 0:
        years -= 1
        months += 12
    
    print(f"\nВаш возраст: {years} лет, {months} месяцев, {days} дней")
    
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    
    days_until = (next_birthday - today).days
    
    print(f"До следующего дня рождения: {days_until} дней")
    if days_until == 0:
        print("С днём рождения! 🎉")


if __name__ == "__main__":
    calculate_age()