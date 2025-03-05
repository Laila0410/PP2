import os

# Открываем файл
with open("text.txt") as f:
    # Читаем все строки файла
    lines = f.readlines()

# Выводим количество строк
print("Количество строк в файле:", len(lines))