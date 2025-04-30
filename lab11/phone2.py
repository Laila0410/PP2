import psycopg2 # Импортируем библиотеку psycopg2 для работы с PostgreSQL
# Подключение к базе данных
conn = psycopg2.connect( # Создаётся соединение с базой данных phonebook через указанные параметры (host, user, password, port).
    host="localhost", # Адрес сервера БД
    dbname="phonebook",  
    user="postgres", 
    password="postgres", 
    port="5435", 
)
def search_phonebook(pattern): # Функция для поиска в телефонной книге по шаблону
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,)) # вызывает функцию в PostgreSQL с именем search_phonebook, которая возвращает данные. %s - параметр для безопасной подстановки значения (защита от SQL-инъекций)
        return cur.fetchall() # Получает все строки, которые вернул запрос.

def insert_or_update_user(first_name, phone): # Функция для вставки или обновления пользователя
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("CALL insert_or_update_user(%s, %s)", (first_name, phone)) #  Вызывается хранимая процедура PostgreSQL insert_or_update_user, которая принимает имя и номер телефона. Отправляет SQL-запрос к подключённой базе данных
        conn.commit() # Сохраняются все изменения в базе данных (иначе они не применятся).

def insert_multiple_users(user_list): # Функция для вставки нескольких пользователей
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        for user in user_list:  # Проходим по каждому пользователю в списке
            try: # Пытаемся выполнить вставку или обновление
                first_name, phone = user.split(',') # Разделяем строку на имя и телефон
                if not phone.strip().isdigit(): # Проверяем, является ли телефон номером
                    print(f"Қате телефон нөмірі: {phone}") # Если нет, выводим сообщение об ошибке
                    continue # Переходим к следующему пользователю
                cur.execute("CALL insert_or_update_user(%s, %s)", (first_name.strip(), phone.strip())) # Вызывается хранимая процедура PostgreSQL insert_or_update_user, которая принимает имя и номер телефона.
            except ValueError: # Если произошла ошибка при разбиении строки
                print(f"Қате енгізу форматы: {user}") 
        conn.commit() # Сохраняются все изменения в базе данных (иначе они не применятся).

def get_phonebook_page(limit, offset): # Функция для получения страницы телефонной книги
    with conn.cursor() as cur: # Создаётся курсор для выполнения SQL-запросов.
        cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset)) # Вызывается функция get_phonebook_page, которая возвращает записи с указанными лимитом и смещением.
        # limit - максимальное количество записей на странице
        return cur.fetchall() # Получает все строки, которые вернул запрос.

def delete_user(input_text): # Функция для удаления пользователя по имени или телефону
    with conn.cursor() as cur: 
        cur.execute("CALL delete_user(%s)", (input_text,)) # Вызывается хранимая процедура PostgreSQL delete_user, которая принимает значение для удаления.
        conn.commit()   # Сохраняются все изменения в базе данных (иначе они не применятся).
#3
# Негізгі функция
def main():     # Основная функция, которая запускает программу
    while True: # Бесконечный цикл, который будет работать до тех пор, пока не будет вызван выход
        print("\nМеню:")
        print("1. Жаңа пайдаланушы қосу немесе телефонды жаңарту")
        print("2. Көптеген пайдаланушыларды қосу")
        print("3. Деректерді үлгі бойынша іздеу")
        print("4. Беттеу арқылы деректерді сұрау")
        print("5. Деректерді жою")
        print("6. Шығу")
        choice = input("Сіз қай опцияны таңдайсыз? ")

        if choice == '1':
            first_name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update_user(first_name, phone)    # Вызывается хранимая процедура PostgreSQL insert_or_update_user, которая принимает имя и номер телефона.

        elif choice == '2':
            user_input = input("Пайдаланушылар тізімін енгізіңіз (мысалы: Айжан,87011234567;Нурик,87018889900): ")
            user_list = user_input.split(';') # Разделяем строку на список пользователей по точке с запятой
            insert_multiple_users(user_list) # Вызывает функцию для массовой вставки пользователей в телефонную книгу.

        elif choice == '3':
            pattern = input("Үлгі бойынша іздеу (атауы немесе телефон нөмірі): ")
            results = search_phonebook(pattern) # Вызывает функцию поиска по шаблону.
            for row in results: # Для каждой строки в результатах:
                print(row)  # Выводит строку с данными пользователя.

        elif choice == '4':
            limit = int(input("Шектеу саны (limit): "))
            offset = int(input("Бастапқы орын (offset): "))
            results = get_phonebook_page(limit, offset) # Вызывает функцию получения страницы телефонной книги.
            for row in results: 
                print(row) 

        elif choice == '5':
            input_text = input("Пайдаланушы аты немесе телефон нөмірі бойынша деректерді жою: ") 
            delete_user(input_text) # Вызывает функцию удаления пользователя по имени или телефону.

        elif choice == '6': # Выход из программы
            break

        else:
            print("Неверный ввод!")

    conn.close() # Закрывает соединение с базой данных после завершения работы программы.   
#2
if __name__ == "__main__": # Проверяет, что данный файл является основным модулем, и запускает основную функцию программы.
    main() # Запускает основную функцию программы, если файл запускается напрямую.
