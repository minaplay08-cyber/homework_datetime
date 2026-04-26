"""
Задача 2: Планировщик задач
"""
from datetime import date, datetime, timedelta


class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
    
    def __repr__(self):
        return f"Task('{self.title}', {self.due_date.strftime('%d.%m.%Y')})"


def parse_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y").date()


def add_task(tasks):
    title = input("Название задачи: ").strip()
    due_str = input("Срок выполнения (ДД.ММ.ГГГГ): ").strip()
    try:
        due_date = parse_date(due_str)
        tasks.append(Task(title, due_date))
        print(f"Задача '{title}' добавлена на {due_str}")
    except ValueError:
        print("Ошибка: неверный формат даты")


def show_today_tasks(tasks):
    today = date.today()
    today_tasks = [t for t in tasks if t.due_date == today]
    print("\n" + "=" * 50)
    print("ЗАДАЧИ НА СЕГОДНЯ")
    print("=" * 50)
    if today_tasks:
        for t in today_tasks:
            print(f"  • {t.title}")
    else:
        print("Нет задач на сегодня")


def show_overdue_tasks(tasks):
    today = date.today()
    overdue = [t for t in tasks if t.due_date < today]
    print("\n" + "=" * 50)
    print("ПРОСРОЧЕННЫЕ ЗАДАЧИ")
    print("=" * 50)
    if overdue:
        for t in overdue:
            print(f"  • {t.title} ({(today - t.due_date).days} дн. просрочки)")
    else:
        print("Нет просроченных задач")


def show_upcoming_tasks(tasks):
    today = date.today()
    week_later = today + timedelta(days=7)
    upcoming = [t for t in tasks if today < t.due_date <= week_later]
    print("\n" + "=" * 50)
    print("ЗАДАЧИ НА БЛИЖАЙШИЕ 7 ДНЕЙ")
    print("=" * 50)
    if upcoming:
        for t in sorted(upcoming, key=lambda x: x.due_date):
            days = (t.due_date - today).days
            print(f"  • {t.title} (через {days} дн.)")
    else:
        print("Нет задач на ближайшую неделю")


def show_all_tasks(tasks):
    print("\n" + "=" * 50)
    print("ВСЕ ЗАДАЧИ")
    print("=" * 50)
    for t in sorted(tasks, key=lambda x: x.due_date):
        status = "✓" if t.due_date >= date.today() else "✗"
        print(f"  [{status}] {t.title} - {t.due_date.strftime('%d.%m.%Y')}")


def task_manager():
    tasks = [
        Task("Сдать лабораторную", date.today() + timedelta(days=3)),
        Task("Подготовить отчёт", date.today() + timedelta(days=7)),
        Task("Купить продукты", date.today()),
    ]
    
    print("=" * 50)
    print("ПЛАНИРОВЩИК ЗАДАЧ")
    print("=" * 50)
    
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи на сегодня")
        print("3. Показать просроченные")
        print("4. Показать на ближайшие 7 дней")
        print("5. Показать все задачи")
        print("0. Выход")
        
        choice = input("\nВыбор: ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_today_tasks(tasks)
        elif choice == "3":
            show_overdue_tasks(tasks)
        elif choice == "4":
            show_upcoming_tasks(tasks)
        elif choice == "5":
            show_all_tasks(tasks)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    task_manager()