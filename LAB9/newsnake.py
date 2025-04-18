import random
import pygame
import sys

# Инициализация Pygame
pygame.init()
width, height = 500, 500
cell_size = 10
score = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Simple Snake | Score: {score}")

# Загрузка изображений
try:
    snake_head_image = pygame.image.load("resources/snake.png").convert_alpha()
    snake_head_image = pygame.transform.scale(snake_head_image, (cell_size, cell_size))
    food_image = pygame.image.load("resources/appleee.png").convert_alpha()
    food_image = pygame.transform.scale(food_image, (cell_size, cell_size))
except pygame.error as e:
    print(f"Ошибка загрузки изображений: {e}")
    sys.exit()

# Цвета
black = (0, 0, 0)
red = (255, 0, 0)  # Цвет тела змейки

# Начальные параметры змейки
speed = 10
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'LEFT'
change_to = direction

# Генерация еды с разными весами
food_weights = [1, 2, 3]  # Возможные очки за еду
food_weight = random.choice(food_weights)  # Текущий вес еды

# Таймер для еды
food_timer = 5000  # Время исчезновения еды (в миллисекундах)
last_food_time = pygame.time.get_ticks()

# Функция генерации новой еды
def generate_food():
    global food_pos, food_weight, last_food_time
    food_pos = [random.randrange(0, width//cell_size)*cell_size,
                random.randrange(0, height//cell_size)*cell_size]
    food_weight = random.choice(food_weights)  # Новый вес еды
    last_food_time = pygame.time.get_ticks()  # Обновление таймера

generate_food()

clock = pygame.time.Clock()

running = True
while running:
    # Обработка событий (выход, управление)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    
    # Обновление направления
    direction = change_to

    # Движение змейки
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    # Проверка на столкновение со стеной
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    # Обновление тела змейки
    snake_body.insert(0, list(snake_pos))

    # Проверка съедения еды
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += food_weight  # Добавляем очки по весу еды
        generate_food()  # Генерируем новую еду
    else:
        snake_body.pop()

    # Проверка времени жизни еды
    if pygame.time.get_ticks() - last_food_time > food_timer:
        generate_food()  # Перегенерация еды после истечения таймера

    pygame.display.set_caption(f"Simple Snake | Score: {score}")

    # Отрисовка экрана
    screen.fill(black)

    # Отрисовка тела змейки
    for block in snake_body[1:]:
        pygame.draw.rect(screen, red, pygame.Rect(block[0], block[1], cell_size, cell_size))

    # Отрисовка головы змейки
    screen.blit(snake_head_image, (snake_body[0][0], snake_body[0][1]))

    # Отрисовка еды
    screen.blit(food_image, (food_pos[0], food_pos[1]))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
