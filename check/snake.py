import pygame # Импортируем библиотеку Pygame для создания игры
import random # Импортируем библиотеку random для генерации случайных чисел
import psycopg2 # Импортируем библиотеку psycopg2 для работы с PostgreSQL
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)

snake_block = 10 # Размер блока змейки
snake_speed = 15  # Скорость змейки
# Устанавливаем соединение с базой данных PostgreSQL
conn = psycopg2.connect( # Указываем параметры подключения
    dbname="snake",     
    user="postgres",       
    password="postgres", 
    host="localhost",
    port="5435"
)
cur = conn.cursor() # Создаём курсор для выполнения SQL-запросов Проще говоря, это как "перо", которым ты пишешь запрос в базу данных.

def your_score(screen, score, score_font): # Функция для отображения счёта
    value = score_font.render("Ваши очки: " + str(score), True, BLACK) # Создаём текст с очками
    screen.blit(value, [0, 0]) # Отображаем текст на экране, blit используется для отображения одного изображения на другом

def message(screen, msg, color, font_style): # Функция для отображения сообщения
    mesg = font_style.render(msg, True, color) # Создаём текст сообщения Метод render в Pygame используется для создания изображения текста
    screen.blit(mesg, [WIDTH / 8, HEIGHT / 2]) # Отображаем текст на экране


def our_snake(screen, snake_block, snake_list): # Функция для отображения змейки
    for x in snake_list: # Проходим по всем элементам списка змейки
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block]) # Рисуем прямоугольник (блок) змейки на экране


def gameLoop(username): # Основная функция игры
    pygame.init()   # Инициализируем Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Устанавливаем размеры окна игры
    pygame.display.set_caption("Snake Game") # Устанавливаем заголовок окна игры
    clock = pygame.time.Clock() # Создаём объект для управления временем

    font_style = pygame.font.SysFont("bahnschrift", 25) # Устанавливаем шрифт для текста которая создаёт объект шрифта
    score_font = pygame.font.SysFont("comicsansms", 35) # Устанавливаем шрифт для счёта

    game_over = False 
    game_close = False # Переменные для отслеживания состояния игры
    x1 = WIDTH / 2 # Начальные координаты змейки
    y1 = HEIGHT / 2 
    x1_change = 0 
    y1_change = 0   

    snake_List = [] # Список для хранения координат блоков змейки
    Length_of_snake = 1 # Начальная длина змейки

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0 # Генерируем случайные координаты для еды
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0 

    while not game_over: # Основной игровой цикл

        while game_close:   # Цикл, который выполняется, когда игра окончена
            screen.fill(BLUE) 
            message(screen, "Вы проиграли! Q - выход | C - заново", RED, font_style) # Отображаем сообщение о проигрыше
            your_score(screen, Length_of_snake - 1, score_font)     # Отображаем счёт
            pygame.display.update() # Обновляем экран

            for event in pygame.event.get(): # Обрабатываем события
                if event.type == pygame.KEYDOWN: # Если нажата клавиша
                    if event.key == pygame.K_q: # Если нажата клавиша Q
                        game_over = True # Выход из игры
                        game_close = False  # Закрываем цикл
                    if event.key == pygame.K_c:     # Если нажата клавиша C
                        gameLoop(username) # Запускаем игру заново

        for event in pygame.event.get(): # Обрабатываем события
            if event.type == pygame.QUIT: # Если нажата кнопка выхода
                game_over = True    # Выход из игры
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:  
                    x1_change = -snake_block    # Изменяем координаты змейки влево
                    y1_change = 0 # Изменяем координаты змейки вверх
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block 
                    y1_change = 0 
                elif event.key == pygame.K_UP: 
                    y1_change = -snake_block # Изменяем координаты змейки вниз
                    x1_change = 0
                elif event.key == pygame.K_DOWN:    
                    y1_change = snake_block # Изменяем координаты змейки вниз
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0: # Проверяем, не вышла ли змейка за границы окна
            game_close = True # Если вышла, то игра окончена
        x1 += x1_change # Изменяем координаты змейки
        y1 += y1_change
        screen.fill(BLUE) 
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block]) # Рисуем еду на экране
        snake_Head = [x1, y1] # Создаём голову змейки
        snake_List.append(snake_Head) # Добавляем голову в список змейки
        if len(snake_List) > Length_of_snake:   # Если длина змейки больше заданной
            del snake_List[0] # Удаляем первый элемент из списка змейки

        for x in snake_List[:-1]: # Проверяем, не столкнулась ли змейка сама с собой 
            if x == snake_Head: # Если голова совпадает с телом
                game_close = True # Игра окончена

        our_snake(screen, snake_block, snake_List) # Отображаем змейку на экране
        your_score(screen, Length_of_snake - 1, score_font) # Отображаем счёт

        pygame.display.update() # Обновляем экран

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0 # Генерируем новые координаты еды
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0 # Генерируем новые координаты еды
            Length_of_snake += 1 # Увеличиваем длину змейки
            save_game_state(username, Length_of_snake - 1, 1, snake_speed, 3, "playing") # Сохраняем состояние игры в базе данных

        clock.tick(snake_speed) # Устанавливаем скорость игры

    pygame.quit() # Закрываем Pygame
    quit()  # Закрываем программу

 
def save_game_state(username, score, level, speed, wall_density, game_state): # Функция для сохранения состояния игры в базе данных
    cur.execute("SELECT user_id FROM users WHERE username = %s;", (username,)) # Получаем ID пользователя из базы данных
    user_id = cur.fetchone()[0] # Извлекаем ID пользователя из результата запроса Возвращает её в виде кортежа (tuple) или None, если строк больше нет
    cur.execute("""  # Сохраняем состояние игры в таблице user_scores
        INSERT INTO user_scores (user_id, score, level, speed, wall_density, game_state) # Вставляем данные в таблицу user_scores
        VALUES (%s, %s, %s, %s, %s, %s); # Указываем, какие данные вставляем
    """, (user_id, score, level, speed, wall_density, game_state)) # Передаём данные в запрос
    conn.commit() # Сохраняем изменения в базе данных
    print("Состояние игры сохранено.") 


def get_user_level(username): # Функция для получения уровня пользователя из базы данных
    cur.execute("SELECT user_id FROM users WHERE username = %s;", (username,)) # Получаем ID пользователя из базы данных
    result = cur.fetchone() # Извлекаем ID пользователя из результата запроса Возвращает её в виде кортежа (tuple) или None, если строк больше нет

    if result: # Если пользователь найден
        user_id = result[0] # Извлекаем ID пользователя из результата запроса
        cur.execute("""  # Получаем уровень пользователя из таблицы user_scores
            SELECT score, level, speed, wall_density  # Извлекаем данные из таблицы user_scores
            FROM user_scores  # Указываем таблицу, из которой извлекаем данные
            WHERE user_id = %s # Указываем, какой пользователь
            ORDER BY timestamp DESC LIMIT 1; # Сортируем по времени и берём последний
        """, (user_id,))
        score_data = cur.fetchone() # Извлекаем данные из результата запроса Возвращает её в виде кортежа (tuple) или None, если строк больше нет

        if score_data: # Если данные найдены
            print(f"Добро пожаловать обратно, {username}!") # Приветствуем пользователя
            print(f"Текущий уровень: {score_data[1]}, Скорость: {score_data[2]}, Стены: {score_data[3]}") # Выводим данные о состоянии игры
            return score_data[1] # Возвращаем уровень пользователя
        else: # Если данные не найдены
            print(f"Добро пожаловать, {username}! Начнём с уровня 1.") # Приветствуем пользователя и начинаем с уровня 1
            return 1 
    else:
        print(f"Пользователь {username} не найден. Создаём нового.")  # Если пользователь не найден, создаём нового
        create_new_user(username) # Создаём нового пользователя
        return 1 


def create_new_user(username): # Функция для создания нового пользователя в базе данных
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id;", (username,)) # Вставляем нового пользователя в таблицу users
    user_id = cur.fetchone()[0] # Извлекаем ID нового пользователя из результата запроса Возвращает её в виде кортежа (tuple) или None, если строк больше нет
    print(f"Создан пользователь {username} с ID {user_id}.") # Выводим сообщение о создании пользователя
    create_new_user_score(user_id) # Создаём начальный счёт для нового пользователя


def create_new_user_score(user_id): # Функция для создания начального счёта для нового пользователя в базе данных
    cur.execute(""" # Вставляем начальный счёт в таблицу user_scores
        INSERT INTO user_scores (user_id, score, level, speed, wall_density) # Вставляем данные в таблицу user_scores
        VALUES (%s, 0, 1, 5, 3); # Указываем, какие данные вставляем
    """, (user_id,)) # Передаём данные в запрос
    conn.commit() # Сохраняем изменения в базе данных


def main(): # Основная функция программы
    username = input("Введите имя пользователя: ") # имя пользователя жазамыз
    current_level = get_user_level(username) # Получаем уровень пользователя из базы данных
    print(f"Вы начинаете с уровня {current_level}") #  сообщение о начале игры шыгарамыз
    gameLoop(username) # Запускаем основную функцию игры


if __name__ == "__main__": # Проверяем, что файл запускается как основная программа
    main() # Запускаем основную функцию программы
""" thats right one """    