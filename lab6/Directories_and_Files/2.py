import os

def check_path_access(path):
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует.")
        return

    print(f"Проверка доступа для пути: {path}")
    if os.access(path, os.R_OK):
        # R = read
        print("Доступ на чтение: Разрешен")
    else:
        print("Доступ на чтение: Запрещен")
    if os.access(path, os.W_OK):
        # W = write
        print("Доступ на запись: Разрешен")
    else:
        print("Доступ на запись: Запрещен")
    if os.access(path, os.X_OK):
        # X = access
        print("Доступ на выполнение: Разрешен")
    else:
        print("Доступ на выполнение: Запрещен")

path = input("Введите путь для проверки: ")

# Вызов функции для проверки доступа
check_path_access(path)