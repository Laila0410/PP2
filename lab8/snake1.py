import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 500, 500
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Snake")

# Загрузка пиксельного рисунка змеи
snake_image = pygame.image.load("snake3.png")
snake_image = pygame.transform.scale(snake_image, (BLOCK_SIZE, BLOCK_SIZE))

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Начальные параметры змеи
snake = [(100, 100)]
direction = (BLOCK_SIZE, 0)  # Движение вправо

# Позиция еды
food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
    
    # Движение змеи
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    # Проверка выхода за границы (телепортация на другую сторону)
    """
    if new_head[0] < 0:
        new_head = (WIDTH - BLOCK_SIZE, new_head[1])
    elif new_head[0] >= WIDTH:
        new_head = (0, new_head[1])
    if new_head[1] < 0:
        new_head = (new_head[0], HEIGHT - BLOCK_SIZE)
    elif new_head[1] >= HEIGHT:
        new_head = (new_head[0], 0)
    """
    snake.insert(0, new_head)
    
    # Проверка на съедание еды
    if new_head == food:
        food = (random.randint(0, WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()
    
    # Отрисовка еды
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Отрисовка змеи
    for segment in snake:
        screen.blit(snake_image, segment)
    
    # Обновление экрана
    pygame.display.flip()
    clock.tick(10)  # Скорость игры

pygame.quit()
