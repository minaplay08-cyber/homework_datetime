"""
Задача 3: Форматирование дат
"""
from datetime import datetime


MONTHS_RU = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
]

MONTHS_EN = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]


def format_date_russian(date_obj):
    return f"{date_obj.day} {MONTHS_RU[date_obj.month - 1]} {date_obj.year} года"


def format_date_dots(date_obj):
    return date_obj.strftime("%d.%m.%Y")


def format_date_iso(date_obj):
    return date_obj.strftime("%Y-%m-%d")


def format_date_english(date_obj):
    return date_obj.strftime("%b %d, %Y").replace("Jan", "Jan").replace("Feb", "Feb")


def format_date_all(date_input):
    if isinstance(date_input, str):
        date_obj = datetime.strptime(date_input, "%d.%m.%Y").date()
    else:
        date_obj = date_input
    
    return {
        "Русский формат": format_date_russian(date_obj),
        "DD.MM.YYYY": format_date_dots(date_obj),
        "ISO (YYYY-MM-DD)": format_date_iso(date_obj),
        "Английский формат": format_date_english(date_obj)
    }


def demo():
    from datetime import date
    today = date.today()
    
    print("=" * 50)
    print("ФОРМАТИРОВАНИЕ ДАТ")
    print("=" * 50)
    
    formats = format_date_all(today)
    for name, value in formats.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    demo()