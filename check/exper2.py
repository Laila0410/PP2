import psycopg2
import pandas as pd
import chardet
from tabulate import tabulate

def get_db_connection():
    """Устанавливает соединение с базой данных"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Ошибка подключения к базе данных:", e)
        exit()

def detect_file_encoding(file_path):
    """Определяет кодировку файла"""
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read(10000)  # Читаем только первые 10000 байт для определения кодировки
            result = chardet.detect(raw_data)
            return result['encoding']
    except Exception as e:
        print(f"Ошибка при определении кодировки файла: {e}")
        return None

def upload_from_csv(file_path):
    """Загружает данные из CSV файла в базу данных"""
    encoding = detect_file_encoding(file_path)
    if not encoding:
        print("Не удалось определить кодировку файла")
        return False
    
    try:
        # Читаем CSV с определенной кодировкой
        data = pd.read_csv(file_path, encoding=encoding)
        
        # Приводим названия колонок к нижнему регистру и удаляем пробелы
        data.columns = data.columns.str.lower().str.strip()
        
        # Проверяем наличие необходимых колонок
        required_columns = ['name', 'surname', 'phone']
        if not all(col in data.columns for col in required_columns):
            print(f"Ошибка: CSV файл должен содержать колонки: {required_columns}")
            return False
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Подготавливаем данные для вставки
        records = data[['name', 'surname', 'phone']].to_records(index=False)
        
        # Вставляем данные пакетами
        for record in records:
            try:
                cur.execute(
                    "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                    (str(record[0]), str(record[1]), str(record[2]))
            except Exception as e:
                print(f"Ошибка при вставке записи {record}: {e}")
                conn.rollback()
                continue
        
        conn.commit()
        print(f"Успешно загружено {len(data)} записей")
        return True
        
    except Exception as e:
        print(f"Ошибка при обработке CSV файла: {e}")
        return False
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()

def main_menu():
    """Главное меню программы"""
    while True:
        print("\n" + "="*50)
        print("Телефонная книга".center(50))
        print("="*50)
        print("1. Добавить контакт (вручную)")
        print("2. Импорт из CSV файла")
        print("3. Поиск контакта")
        print("4. Обновить контакт")
        print("5. Удалить контакт")
        print("6. Показать все контакты")
        print("7. Выход")
        print("="*50)
        
        choice = input("Выберите действие (1-7): ").strip()
        
        if choice == "1":
            add_contact_manual()
        elif choice == "2":
            file_path = input("Введите путь к CSV файлу: ").strip()
            upload_from_csv(file_path)
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            show_all_contacts()
        elif choice == "7":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова")

# Остальные функции (add_contact_manual, search_contact, update_contact, delete_contact, show_all_contacts)
# должны быть реализованы аналогичным образом с обработкой ошибок

if __name__ == "__main__":
    # Проверяем и создаем таблицу при первом запуске
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                surname VARCHAR(255) NOT NULL, 
                phone VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")
    finally:
        if 'conn' in locals():
            cur.close()
            conn.close()
    
    # Запускаем главное меню
    main_menu()