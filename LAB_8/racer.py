import pygame
import sys #взаимодействие с интерпретатором Python
from pygame.locals import *
import random, time
# Инициализация Pygame
pygame.init()

# FPS — количество кадров в секунду
FPS = 60  # Частота обновлений экрана, количество кадров в секунду
FramePerSec = pygame.time.Clock()  # Управление FPS, чтобы поддерживать постоянную скорость игры

# Определяем цвета (RGB формат)
BLUE = (0, 0, 255)  # Синий
RED = (255, 0, 0)  # Красный    
GREEN = (0, 255, 0)  # Зелёный
BLACK = (0, 0, 0)  # Чёрный
WHITE = (255, 255, 255)  # Белый

# Прочие переменные
SCREEN_WIDTH = 400  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
SPEED = 3  # Начальная скорость (скорость движения объектов)
SCORE = 0  # Начальный счёт
COINS = 0  # Начальное количество собранных монет

# Шрифты для текста
font = pygame.font.SysFont("Verdana", 20)  # Основной шрифт для текста
font_small = pygame.font.SysFont("Verdana", 20)  # Маленький шрифт для отображения счёта
game_over = font.render("Game Over", True, BLACK)  # Создаём текст "Game Over" для экрана окончания игры
"""
Метод font.render() в Pygame используется для создания изображения (или поверхности), 
на которой будет отображаться текст.
 Это изображение затем можно вывести на экран с помощью метода blit().
"""
# Загружаем изображение фона (дорога)
background = pygame.image.load("resources/road.png")

# Создаём экран с размерами 400x600
screen = pygame.display.set_mode((400, 600))  
screen.fill(WHITE)  # Заполняем экран белым цветом
pygame.display.set_caption("Racer")  # Название окна игры


# Класс для врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Наследуем от класса Sprite
        self.image = pygame.image.load("resources/Enemy.png")  # Загружаем изображение врага
        self.rect = self.image.get_rect()  # Получаем прямоугольник (объект для столкновений)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Начальная позиция врага (с случайным X)

    def move(self):
        global SCORE  # Увеличиваем счёт, если враг выходит за экран
        self.rect.move_ip(0, SPEED)  # Враг двигается вниз по экрану с текущей скоростью
        if (self.rect.top > 600):  # Если враг выходит за нижнюю границу экрана
            SCORE += 1  # Увеличиваем счёт
            self.rect.top = 0  # Перемещаем врага обратно вверх
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Новый случайный X для врага

# Класс для монет
c1, c2, c3, c4, c5 = False, False, False, False, False  # Флаги для увеличения скорости игры при наборе монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Наследуем от класса Sprite
        self.image = pygame.image.load("resources/coin2.png")  # Загружаем изображение монеты
        self.image = pygame.transform.scale(self.image, (40, 40))  # Масштабируем изображение монеты
        self.rect = self.image.get_rect()  # Получаем прямоугольник для монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))  # Позиция монеты

    def move(self):
        global COINS, SPEED  # Обновляем количество монет и скорость игры
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3  # Если монета ближе к верхней части экрана, даём 3 очка
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2  # Если монета чуть ниже, даём 2 очка
        else:
            COINS += 1  # Если монета ближе к нижней части экрана, даём 1 очко

        # Увеличиваем скорость игры при достижении определённого количества монет
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1
            c5 = True

        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)  # self.rect.top: задаёт случайную вертикальную позицию для монеты.
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))  # устанавливает случайную горизонтальную и вертикальную позицию для монеты на экране.

# Класс для игрока
class Player(pygame.sprite.Sprite): #функций для работы с изображениями и их позиционированием:
    def __init__(self):
        super().__init__()  # Наследуем от класса Sprite
        self.image = pygame.image.load("resources/player.png")  # Загружаем изображение игрока
        self.rect = self.image.get_rect()  # Получаем прямоугольник для игрока
        self.rect.center = (160, 520)  # Начальная позиция игрока внизу экрана

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if self.rect.left > 0:  # Если игрок не выходит за левую границу
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Двигаем игрока влево
        if self.rect.right < SCREEN_WIDTH:  # Если игрок не выходит за правую границу
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Двигаем игрока вправо
        if self.rect.top > 0:  # Если игрок не выходит за верхнюю границу
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)  # Двигаем игрока вверх
        if self.rect.bottom < SCREEN_HEIGHT:  # Если игрок не выходит за нижнюю границу
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)  # Двигаем игрока вниз

# Создаём объекты для игрока, врага и монеты
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()  # Группа врагов
enemies.add(E1)  # Добавляем врага в группу
coinss = pygame.sprite.Group()  # Группа монет
coinss.add(C1)  # Добавляем монету в группу
all_sprites = pygame.sprite.Group()  # Общая группа всех спрайтов
all_sprites.add(P1)  # Добавляем игрока
all_sprites.add(E1)  # Добавляем врага
all_sprites.add(C1)  # Добавляем монету

# Создаём событие для увеличения скорости игры
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Устанавливаем таймер для увеличения скорости каждую секунду

# Функция для экрана окончания игры
def game_over_screen():
    screen.fill(RED)  # Заполняем экран красным цветом
    screen.blit(game_over, (30, 250))  # Отображаем текст "Game Over"
    pygame.display.update()  # Обновляем экран

    while True:
        for event in pygame.event.get():  # Проверяем события
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Если нажата клавиша пробела, перезапускаем игру
                    return True
                elif event.key == K_ESCAPE:  # Если нажата клавиша ESC, закрываем игру
                    return False

# Функция для обработки аварии (пауза перед продолжением игры)
def handle_crash():
    time.sleep(2)  # Пауза 2 секунды

# Инициализация фона
background_y = 0  # Координаты для фона

# Главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # Увеличиваем скорость игры
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Проверка на столкновение игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()  # Обработка столкновения
        if not continue_game:
            pygame.quit()
            sys.exit()

    # Прокрутка фона
    background_y = (background_y + SPEED) % background.get_height()

    # Отображение фона
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Отображение счёта
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    # Отображение монет
    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Двигаем и перерисовываем все спрайты
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        # Если игрок собирает монеты
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()  # Перемещаем монету
        else:
            entity.move()

    # Двигаем врагов
    for enemy in enemies:
        enemy.move()

    # Двигаем монеты
    for coin in coinss:
        coin.rect.y += SPEED  # Двигаем монеты вниз

        # Если монета выходит за экран, перерисовываем её
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height  # Перемещаем монету обратно в верхнюю часть экрана
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)  # Новый случайный X

    pygame.display.update()  # Обновляем экран
    FramePerSec.tick(FPS)  # Ограничиваем количество кадров в секунду
