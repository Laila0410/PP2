from datetime import datetime, timedelta
""" 
Этот код импортирует два класса (datetime и timedelta) из модуля datetime.

"""
# орысша кириллицага аударады
# import sys

# sys.stdout.reconfigure(encoding='utf-8')

# Получаем сегодняшнюю дату
today = datetime.today()

# Вычитаем 5 дней
five_days_ago = today - timedelta(days=5)

print("Сегодня:", today.strftime("%y.%m.%d"))
print("5 дней назад:", five_days_ago.strftime("%y.%m.%d"))
"""
datetime.today() получает текущую дату и время.работает с датами и временем (год, месяц, день, час, минута и т. д.).
timedelta(days=5) создает разницу в 5 дней.хранит разницу между датами (например, 5 дней или 3 часа).
today - timedelta(days=5) вычитает 5 дней из текущей даты.
strftime("%Y-%m-%d") форматирует дату в удобный вид.

"""