import random
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана и игры
width, height = 500, 500  # Размеры экрана
cell_size = 10  # Размер клетки, в которой будет двигаться змейка
score = 0  # Начальный счёт
screen = pygame.display.set_mode((width, height))  # Устанавливаем размеры окна
pygame.display.set_caption(f"Simple Snake_score:{score}")  # Заголовок окна

# Загрузка изображений для змейки и еды
try:
    snake_head_image = pygame.image.load("resources/snake.png").convert_alpha()  # Загружаем изображение головы змейки
    snake_head_image = pygame.transform.scale(snake_head_image, (cell_size, cell_size))  # Масштабируем изображение до размера клетки
    food_image = pygame.image.load("resources/appleee.png").convert_alpha()  # Загружаем изображение еды
    food_image = pygame.transform.scale(food_image, (cell_size, cell_size))  # Масштабируем изображение еды до размера клетки
except pygame.error as e:  # Обработка ошибки загрузки изображений
    print(f"Ошибка загрузки изображений: {e}")
    sys.exit()

# Определение цветов
black = (0, 0, 0)  # Цвет фона (чёрный)
red = (255, 0, 0)  # Цвет тела змейки (красный)

# Начальные параметры змейки
speed = 10  # Начальная скорость игры
snake_pos = [100, 100]  # Начальная позиция головы змейки
snake_body = [[100, 100], [80, 100], [60, 100]]  # Тело змейки (список, состоящий из её сегментов)
direction = 'LEFT'  # Направление движения змейки (начинаем с левого)
change_to = direction  # Направление, в которое нужно двигаться в следующем цикле
food_pos = [random.randrange(0, width//cell_size)*cell_size,  # Начальная позиция еды (случайное расположение)
            random.randrange(0, height//cell_size)*cell_size]

# Создание объекта "часы" для контроля FPS
clock = pygame.time.Clock()

running = True  # Флаг работы игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна игры
            running = False
        elif event.type == pygame.KEYDOWN:  # Проверка нажатия клавиш
            # Обработка нажатых клавиш (изменение направления змейки)
            if event.key == pygame.K_UP and direction != 'DOWN':  # Нельзя двигаться в противоположное направление
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    direction = change_to  # Обновляем направление змейки

    # Движение змейки
    if direction == 'UP':
        snake_pos[1] -= cell_size  # Двигаем змейку вверх
    elif direction == 'DOWN':
        snake_pos[1] += cell_size  # Двигаем змейку вниз
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size  # Двигаем змейку влево
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size  # Двигаем змейку вправо
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    # Обновление тела змейки
    snake_body.insert(0, list(snake_pos))  # Добавляем новый сегмент в голову змейки
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:  # Проверка, съела ли змейка еду
        food_pos = [random.randrange(0, width//cell_size)*cell_size,  # Создаём новую еду в случайной позиции
                    random.randrange(0, height//cell_size)*cell_size]
        score += 1  # Увеличиваем счёт
    else:
        snake_body.pop()  # Если еда не съедена, удаляем последний сегмент из тела змейки

    pygame.display.set_caption(f"Simple Snake_score:{score}")  # Обновляем заголовок с текущим счётом

    # Отрисовка
    screen.fill(black)  # Заполняем экран чёрным фоном
    
    # Отрисовка тела змейки (красные квадраты)
    for block in snake_body[1:]:  # Рисуем все сегменты, кроме головы
        pygame.draw.rect(screen, red, pygame.Rect(block[0], block[1], cell_size, cell_size))
    
    # Отрисовка головы змейки (с изображением)
    screen.blit(snake_head_image, (snake_body[0][0], snake_body[0][1]))
    
    # Отрисовка еды (с изображением)
    screen.blit(food_image, (food_pos[0], food_pos[1]))

    pygame.display.flip()  # Обновляем экран
    clock.tick(speed)  # Контроль частоты кадров (скорости игры)

pygame.quit()  # Завершаем Pygame
sys.exit()  # Закрываем программу
