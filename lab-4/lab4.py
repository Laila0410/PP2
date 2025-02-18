"""
📌 Объяснение тем из лабораторной работы
Ты прошла Python Iterators, Generators, Scope, Modules, Dates, Math, JSON. Давай разберем каждую тему простыми словами.

1️⃣ Python Iterators (Итераторы)
🔹 Что это?
Итератор — это объект, который можно перебирать по одному элементу.

🔹 Как это работает?

Любой объект, который можно использовать в for — итерируемый.
У таких объектов есть метод __iter__().
Итераторы запоминают, где остановились.
Пример (итерируемый объект list):

python
Copy
Edit
numbers = [1, 2, 3]  # Список — это итерируемый объект

for num in numbers:
    print(num)  # Выведет 1, 2, 3
Пример (создаем итератор вручную):

python
Copy
Edit
numbers = [1, 2, 3]
iterator = iter(numbers)  # Создаем итератор

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
Если вызвать next() еще раз — будет ошибка, потому что элементы закончились.

2️⃣ Python Generators (Генераторы)
🔹 Что это?
Генератор — это ленивый итератор. Он создает значения по мере необходимости и не хранит их в памяти.

🔹 Как это работает?

Вместо return используется yield.
Генератор можно перебирать for-ом.
Значения вычисляются по мере запроса.
Пример генератора:

python
Copy
Edit
def count_up_to(n):
    num = 1
    while num <= n:
        yield num  # Запоминает текущее состояние
        num += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
Когда значения закончились, следующий next() вызовет ошибку.

⚡ Зачем нужны генераторы?
🔹 Они экономят память!
Например, range(1000000) не создает список, а только "генерирует" числа.

3️⃣ Python Scope (Область видимости переменных)
🔹 Что это?
Scope — это где переменная доступна.

🔹 Виды областей видимости:

Local (локальная) — внутри функции.
Enclosing (вложенная) — внутри вложенной функции.
Global (глобальная) — в основном коде.
Built-in (встроенная) — встроенные функции Python (print, len и т. д.).
🔹 Пример:

python
Copy
Edit
x = 10  # Глобальная переменная

def my_function():
    x = 5  # Локальная переменная (только в этой функции)
    print(x)  # Выведет 5

my_function()
print(x)  # Выведет 10, потому что глобальная переменная не изменилась
Пример global:

python
Copy
Edit
x = 10

def change_x():
    global x  # Позволяет изменять глобальную переменную
    x = 5

change_x()
print(x)  # Выведет 5
4️⃣ Python Modules (Модули)
🔹 Что это?
Модуль — это просто файл с кодом Python, который можно использовать в других программах.

🔹 Импорт модулей:

python
Copy
Edit
import math  # Импортируем модуль math

print(math.sqrt(25))  # 5.0
🔹 Создание своего модуля:

Создай файл mymodule.py с таким кодом:
python
Copy
Edit
def greet(name):
    return f"Hello, {name}!"
В другом файле main.py импортируй его:
python
Copy
Edit
import mymodule

print(mymodule.greet("Alice"))  # Выведет: Hello, Alice!
5️⃣ Python Dates (Работа с датами)
🔹 Что это?
Python умеет работать с датами через datetime.

🔹 Пример:

python
Copy
Edit
import datetime

now = datetime.datetime.now()  # Получить текущее время
print(now)  # Например: 2025-02-18 18:30:45.123456

# Создать конкретную дату
birthday = datetime.datetime(2000, 5, 20)
print(birthday)  # 2000-05-20 00:00:00
🔹 Форматирование дат (strftime)

python
Copy
Edit
print(now.strftime("%Y-%m-%d"))  # 2025-02-18
print(now.strftime("%H:%M:%S"))  # 18:30:45
6️⃣ Python Math (Математические операции)
🔹 Что это?
Python умеет делать сложные математические вычисления через модуль math.

🔹 Примеры:

python
Copy
Edit
import math

print(math.sqrt(16))  # 4.0 (Квадратный корень)
print(math.pow(2, 3))  # 8.0 (Возведение в степень)
print(math.pi)  # 3.141592653589793
print(math.ceil(4.2))  # 5 (Округление вверх)
print(math.floor(4.8))  # 4 (Округление вниз)
7️⃣ Python JSON (Работа с JSON)
🔹 Что это?
JSON (JavaScript Object Notation) — это формат хранения данных, похожий на словари Python.

🔹 Загрузка JSON из файла:

python
Copy
Edit
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Загружает JSON в словарь Python

print(data)  # Теперь это обычный словарь
🔹 Конвертация словаря Python в JSON:

python
Copy
Edit
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(person, indent=4)  # Преобразуем в JSON-строку
print(json_string)
Выведет:

json
Copy
Edit
{
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
🔹 Итог
Тема	Что это?
Iterators	Перебираемые объекты (next())
Generators	Итераторы, создающие значения yield
Scope	Локальные и глобальные переменные
Modules	Импорт и создание модулей
Dates	Работа с датами datetime
Math	Математические операции math
JSON	Чтение и запись JSON-файлов



"""