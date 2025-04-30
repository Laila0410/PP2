import psycopg2
import pandas as pd
import chardet
from tabulate import tabulate
import sys

try:
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port="5432"
    )
    print("Подключение успешно!")
    print(f"Кодировка соединения: {conn.encoding}")
    conn.close()
except Exception as e:
    print(f"Ошибка: {e}")

def initialize_database(conn):
    """Инициализирует таблицу phonebook"""
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    user_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    surname VARCHAR(255) NOT NULL,
                    phone VARCHAR(255) NOT NULL UNIQUE
                )
            """)
            conn.commit()
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")
        conn.rollback()
        sys.exit(1)

def main_menu():
    """Отображает главное меню"""
    print("\n" + "="*50)
    print("Телефонная книга".center(50))
    print("="*50)
    print("1. Добавить контакт")
    print("2. Обновить контакт")
    print("3. Поиск контактов")
    print("4. Удалить контакт")
    print("5. Показать все контакты")
    print("6. Выйти")
    print("="*50)
    return input("Выберите действие (1-6): ").strip()

def add_contact(conn):
    """Добавляет новый контакт"""
    print("\nДобавление контакта:")
    print("1. Ввести вручную")
    print("2. Загрузить из CSV")
    choice = input("Выберите вариант (1/2): ").strip()
    
    if choice == "1":
        name = input("Имя: ")
        surname = input("Фамилия: ")
        phone = input("Телефон: ")
        
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                    (name, surname, phone)
                )
                conn.commit()
                print("Контакт успешно добавлен!")
        except psycopg2.IntegrityError:
            print("Ошибка: контакт с таким телефоном уже существует")
            conn.rollback()
        except Exception as e:
            print(f"Ошибка при добавлении: {e}")
            conn.rollback()
    
    elif choice == "2":
        filepath = input("Введите путь к CSV файлу: ")
        try:
            # Определяем кодировку файла
            with open(filepath, 'rb') as f:
                result = chardet.detect(f.read())
            
            # Читаем файл с определенной кодировкой
            df = pd.read_csv(filepath, encoding=result['encoding'])
            
            # Проверяем наличие нужных столбцов
            if not all(col in df.columns for col in ['name', 'surname', 'phone']):
                print("Ошибка: CSV файл должен содержать колонки 'name', 'surname' и 'phone'")
                return
            
            # Добавляем данные в базу
            with conn.cursor() as cur:
                for _, row in df.iterrows():
                    try:
                        cur.execute(
                            "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                            (row['name'], row['surname'], row['phone'])
                        )
                    except psycopg2.IntegrityError:
                        print(f"Пропуск дубликата: {row['phone']}")
                        continue
                conn.commit()
                print(f"Успешно добавлено {len(df)} контактов")
        except Exception as e:
            print(f"Ошибка при обработке CSV: {e}")
            conn.rollback()

def update_contact(conn):
    """Обновляет существующий контакт"""
    print("\nОбновление контакта:")
    phone = input("Введите телефон контакта для обновления: ")
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
            contact = cur.fetchone()
            
            if not contact:
                print("Контакт не найден")
                return
            
            print("\nТекущие данные контакта:")
            print(f"ID: {contact[0]}")
            print(f"Имя: {contact[1]}")
            print(f"Фамилия: {contact[2]}")
            print(f"Телефон: {contact[3]}")
            
            print("\nЧто вы хотите изменить?")
            print("1. Имя")
            print("2. Фамилия")
            print("3. Телефон")
            print("4. Все данные")
            choice = input("Выберите вариант (1-4): ").strip()
            
            new_name, new_surname, new_phone = contact[1], contact[2], contact[3]
            
            if choice in ["1", "4"]:
                new_name = input("Новое имя: ")
            if choice in ["2", "4"]:
                new_surname = input("Новая фамилия: ")
            if choice in ["3", "4"]:
                new_phone = input("Новый телефон: ")
            
            cur.execute(
                "UPDATE phonebook SET name = %s, surname = %s, phone = %s WHERE user_id = %s",
                (new_name, new_surname, new_phone, contact[0])
            )
            conn.commit()
            print("Контакт успешно обновлен!")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")
        conn.rollback()

def search_contacts(conn):
    """Поиск контактов"""
    print("\nПоиск контактов:")
    print("1. По ID")
    print("2. По имени")
    print("3. По фамилии")
    print("4. По телефону")
    print("5. Показать все")
    choice = input("Выберите вариант поиска (1-5): ").strip()
    
    try:
        with conn.cursor() as cur:
            if choice == "1":
                user_id = input("Введите ID: ")
                cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (user_id,))
            elif choice == "2":
                name = input("Введите имя: ")
                cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
            elif choice == "3":
                surname = input("Введите фамилию: ")
                cur.execute("SELECT * FROM phonebook WHERE surname ILIKE %s", (f"%{surname}%",))
            elif choice == "4":
                phone = input("Введите телефон: ")
                cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
            elif choice == "5":
                cur.execute("SELECT * FROM phonebook")
            else:
                print("Неверный выбор")
                return
            
            contacts = cur.fetchall()
            if contacts:
                print("\nРезультаты поиска:")
                print(tabulate(
                    contacts,
                    headers=["ID", "Имя", "Фамилия", "Телефон"],
                    tablefmt="fancy_grid"
                ))
            else:
                print("Контакты не найдены")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")

def delete_contact(conn):
    """Удаляет контакт"""
    print("\nУдаление контакта:")
    phone = input("Введите телефон контакта для удаления: ")
    
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            if cur.rowcount > 0:
                conn.commit()
                print("Контакт успешно удален")
            else:
                print("Контакт не найден")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
        conn.rollback()

def main():
    """Основная функция программы"""
    conn = create_connection()
    initialize_database(conn)
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            add_contact(conn)
        elif choice == "2":
            update_contact(conn)
        elif choice == "3":
            search_contacts(conn)
        elif choice == "4":
            delete_contact(conn)
        elif choice == "5":
            search_contacts(conn)  # Показываем все контакты
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова")
        
        input("\nНажмите Enter чтобы продолжить...")
    
    conn.close()

if __name__ == "__main__":
    main()