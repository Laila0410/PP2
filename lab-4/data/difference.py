import datetime

#try:
    # Ввод дат
y, m, d = map(int, input("(year month day): ").split())
y1, m1, d1 = map(int, input("(year month day): ").split())

    # Вычисляем разницу
dif = datetime.datetime(y1, m1, d1) - datetime.datetime(y, m, d)
#datetime.datetime(y1, m1, d1) – создаёт объект даты и времени с годом y1, месяцем m1 и днём d1.
print("difference:", dif)

#except ValueError:
#    print("Ошибка! Введите дату в формате: ГГГГ ММ ДД")
