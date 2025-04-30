import psycopg2
import csv
from psycopg2 import sql

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",    # ← должно совпадать с именем БД!
    user="postgres",
    password="postgres",
    port="5435"            # ← проверь порт (5432 — стандартный)
)

# Создание таблицы PhoneBook
def create_table():
    with conn.cursor() as cur:
        # Удаляем таблицу, если она существует
        cur.execute("DROP TABLE IF EXISTS phonebook")
        # Создаем новую таблицу с правильными столбцами
        cur.execute("""
            CREATE TABLE phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                phone VARCHAR(20) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print("Таблица phonebook создана заново")

# Способ 1: Загрузка данных из CSV файла
def upload_from_csv(filename):
    with conn.cursor() as cur:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Пропускаем заголовок, если он есть
            for row in reader:
                first_name, last_name, phone = row
                cur.execute(
                    "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
                    (first_name, last_name, phone)
                )
        conn.commit()
        print(f"Данные из файла {filename} загружены")

# Способ 2: Ввод данных с консоли
def input_from_console():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию (необязательно): ")
    phone = input("Введите телефон: ")
    
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) ON CONFLICT (phone) DO NOTHING",
            (first_name, last_name, phone)
        )
        conn.commit()
        print("Данные добавлены")

# Обновление данных
def update_data():
    print("1. Изменить имя")
    print("2. Изменить телефон")
    choice = input("Выберите действие: ")
    
    if choice == '1':
        phone = input("Введите телефон для поиска: ")
        new_name = input("Введите новое имя: ")
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                (new_name, phone)
            )
            conn.commit()
            print("Имя обновлено")
    elif choice == '2':
        old_phone = input("Введите старый телефон: ")
        new_phone = input("Введите новый телефон: ")
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE phone = %s",
                (new_phone, old_phone)
            )
            conn.commit()
            print("Телефон обновлен")

# Запрос данных с фильтрами
def query_data():
    print("1. Показать все записи")
    print("2. Поиск по имени")
    print("3. Поиск по телефону")
    print("4. Поиск по фамилии")
    choice = input("Выберите действие: ")
    
    with conn.cursor() as cur:
        if choice == '1':
            cur.execute("SELECT * FROM phonebook")
        elif choice == '2':
            name = input("Введите имя для поиска: ")
            cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
        elif choice == '3':
            phone = input("Введите телефон для поиска: ")
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        elif choice == '4':
            last_name = input("Введите фамилию для поиска: ")
            cur.execute("SELECT * FROM phonebook WHERE last_name = %s", (last_name,))
        
        rows = cur.fetchall()
        for row in rows:
            print(row)

# Удаление данных
def delete_data():
    print("1. Удалить по имени")
    print("2. Удалить по телефону")
    choice = input("Выберите действие: ")
    
    with conn.cursor() as cur:
        if choice == '1':
            name = input("Введите имя для удаления: ")
            cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
        elif choice == '2':
            phone = input("Введите телефон для удаления: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        
        conn.commit()
        print("Данные удалены")

# Главное меню
def main():
    create_table()
    
    while True:
        print("\n1. Загрузить данные из CSV")
        print("2. Ввести данные вручную")
        print("3. Обновить данные")
        print("4. Поиск данных")
        print("5. Удалить данные")
        print("6. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            filename = input("Введите имя CSV файла: ")
            upload_from_csv(filename)
        elif choice == '2':
            input_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break

    conn.close()

if __name__ == "__main__":
    main()