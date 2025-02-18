import datetime

try:
    # Ввод дат
    y, m, d = map(int, input("Введите первую дату (ГГГГ ММ ДД): ").split())
    y1, m1, d1 = map(int, input("Введите вторую дату (ГГГГ ММ ДД): ").split())

    # Вычисляем разницу
    dif = datetime.datetime(y1, m1, d1) - datetime.datetime(y, m, d)

    print("difference:", dif)

except ValueError:
    print("Ошибка! Введите дату в формате: ГГГГ ММ ДД")
