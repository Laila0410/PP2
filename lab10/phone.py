"""1. Импорт библиотек"""
import psycopg2 #  для подключения Python к базе данных PostgreSQL.
import csv # для чтения файлов формата .csv
"""2. Подключение к базе данных"""
# Подключение к базе данных
conn = psycopg2.connect(  # Создаётся соединение с базой данных phonebook через указанные параметры (host, user, password, port).
    host="localhost",     # Адрес сервера БД
    dbname="phonebook",   # Имя базы данных
    user="postgres",      # Имя пользователя БД
    password="postgres",  # Пароль пользователя
    port="5435",          # Порт подключения
)
"""3. Определение всех функций (ещё не выполняются, просто объявляются):"""
def create_table(): # Создаёт таблицу phonebook, если её ещё нет.
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("""  # SQL-запрос на создание таблицы
            CREATE TABLE IF NOT EXISTS phonebook ( # создаёт таблицу только если она не существует.
                id SERIAL PRIMARY KEY,  # автоинкрементный ID.
                first_name VARCHAR(100) NOT NULL, # имя пользователя.
                phone VARCHAR(15) NOT NULL UNIQUE # телефон пользователя.
            );
        """)
        conn.commit()  # Фиксация изменений в БД

# Вызов функции поиска по шаблону 
def search_by_pattern(pattern): #Выводит записи, в которых имя или телефон похожи на введённый шаблон.
    with conn.cursor() as cur: 
        cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,)) # вызывает функцию в PostgreSQL с именем search_phonebook, которая возвращает данные. %s - параметр для безопасной подстановки значения (защита от SQL-инъекций)
        rows = cur.fetchall() #Получает все строки, которые вернул запрос.
        for row in rows:
            print(row)  # Выводит записи, в которых имя или телефон похожи на введённый шаблон.

# Процедура вставки или обновления пользователя
def insert_or_update(name, phone): # Добавляет нового пользователя или обновляет существующего.
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        # Выполняется SQL-запрос, который вызывает хранимую процедуру insert_or_update_user с параметрами name и phone.
        cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone)) #  Вызывается хранимая процедура PostgreSQL insert_or_update_user, которая принимает имя и номер телефона.
        conn.commit() #  Сохраняются все изменения в базе данных (иначе они не применятся).
        print("Пользователь добавлен или обновлён.") # Выводит сообщение о том, что пользователь добавлен или обновлён.

# Процедура массовой вставки с проверкой
def insert_many(users): # Добавляет нескольких пользователей в телефонную книгу.
    # users - список кортежей (имя, телефон)
    names = [u[0] for u in users]   # Извлекает имена пользователей из списка кортежей.
    phones = [u[1] for u in users] # Извлекает телефоны пользователей из списка кортежей.
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("CALL insert_many_users(%s, %s);", (names, phones)) # Вызывается хранимая процедура PostgreSQL insert_many_users, которая принимает списки имён и телефонов.
        conn.commit() # Сохраняются все изменения в базе данных (иначе они не применятся).

# Пагинация
def paginate(limit, offset): # Выводит записи из телефонной книги с пагинацией.
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset)) # Вызывается функция get_phonebook_page, которая возвращает записи с указанными лимитом и смещением.
        rows = cur.fetchall() # Получает все строки, которые вернул запрос.
        for row in rows: # Выводит записи из телефонной книги с пагинацией.
            print(row)

# Удаление по имени или телефону
def delete_user_by_value(value): # Удаляет пользователя по имени или телефону.
    with conn.cursor() as cur: # 
        cur.execute("CALL delete_user(%s);", (value,)) # Вызывается хранимая процедура PostgreSQL delete_user, которая принимает значение для удаления.
        conn.commit() # Сохраняются все изменения в базе данных (иначе они не применятся).
        print("Пользователь удалён, если был найден.")

def insert_from_csv(filename):  # Загружает данные из CSV файла в телефонную книгу.
    with conn.cursor() as cur: # 
        with open(filename, newline='', encoding='utf-8') as csvfile: # Открывает CSV файл с указанной кодировкой.
            reader = csv.reader(csvfile) # Создаёт объект reader для чтения CSV файла.
            for row in reader: # Для каждой строки в CSV файле:
                try: # Проверяет, что телефонный номер состоит только из цифр.
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1])) # Выполняет SQL-запрос на вставку данных в таблицу phonebook.
                except Exception as e: # Если возникает ошибка (например, дублирование уникального значения), выводит сообщение об ошибке.
                    print(f"Ошибка при добавлении {row}: {e}") # Выводит сообщение об ошибке.
                    conn.rollback()  # Откатывает изменения, если произошла ошибка.
        conn.commit() # Сохраняет все изменения в базе данных (иначе они не применятся).
        print("Данные из CSV загружены!")
"""5. Выполнение main()"""
def main(): # Основная функция программы
    create_table() # Создаёт таблицу phonebook, если её ещё нет.
    while True: # Бесконечный цикл для отображения меню и выполнения действий.
        print("\nМеню:") # Выводит меню программы.
        print("1. Вставить или обновить пользователя") # Вставляет или обновляет пользователя.
        print("2. Массовая вставка")
        print("3. Поиск по шаблону")
        print("4. Пагинация")
        print("5. Удалить по имени или телефону")
        print("6. Загрузить из CSV")
        print("7. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1': 
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update(name, phone) 
        elif choice == '2':
            count = int(input("Сколько пользователей хотите ввести? "))
            users = [] # Создаёт пустой список для хранения пользователей.
            for _ in range(count): 
                name = input("Имя: ")
                phone = input("Телефон: ")
                users.append((name, phone)) # Добавляет кортеж (имя, телефон) в список пользователей.
            insert_many(users) # Вызывает функцию для массовой вставки пользователей в телефонную книгу.
        elif choice == '3':
            pattern = input("Введите часть имени или номера: ")
            search_by_pattern(pattern) # Вызывает функцию поиска по шаблону.
        elif choice == '4':
            limit = int(input("Сколько записей показать? "))
            offset = int(input("С какой позиции начать? "))
            paginate(limit, offset) # Вызывает функцию пагинации.
        elif choice == '5':
            value = input("Введите имя или телефон для удаления: ")
            delete_user_by_value(value) # Вызывает функцию удаления пользователя по имени или телефону.
        elif choice == '6':
            filename = input("Имя CSV файла: ")
            insert_from_csv(filename) # Вызывает функцию загрузки данных из CSV файла.
        elif choice == '7': 
            break # Выход из программы.
        else:
            print("Неверный ввод!")

    conn.close() # Закрывает соединение с базой данных после завершения работы программы.
"""4. Запуск основного блока"""
if __name__ == '__main__': # Запуск программы
    main()
