import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("racer")
clock = pygame.time.Clock()

background = pygame.image.load('resources/road.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_img = pygame.image.load("resources/player.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (60, 80))
enemy_img = pygame.image.load("resources/Enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (60, 80))
coin_img = pygame.image.load("resources/coin2.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

player_speed = 5
score = 0
coins_to_increase_speed = 5  #количество монет для увеличения скорости врагов
base_enemy_speed = 3         #базовая скорость врагов
enemy_speed_increase = 0.5   #увеличение скорости врагов
font = pygame.font.SysFont("Arial", 24)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-80))
        self.speed = player_speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:  # Движение вверх
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:  # Движение вниз
            self.rect.y += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()
        self.speed = base_enemy_speed + random.random() * 2  # Случайная скорость

    def reset(self):
        #Сброс позиции врага
        self.rect.x = random.randint(40, WIDTH-100)
        self.rect.y = random.randint(-600, -100)
        #Увеличиваем скорость в зависимости от набранных очков
        self.speed = base_enemy_speed + (score // coins_to_increase_speed) * enemy_speed_increase + random.random()

    def update(self, enemy_group):        #Обновление позиции врага с проверкой столкновений

        self.rect.y += self.speed
        
        for enemy in enemy_group:        # Проверка столкновений с другими врагами
            if enemy != self and self.rect.colliderect(enemy.rect):
                if self.rect.x < enemy.rect.x:
                    self.rect.x -= 5
                else:
                    self.rect.x += 5
                break
        
        if self.rect.top > HEIGHT:
            self.reset()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.weight = random.choice([1, 1, 1, 2, 2, 3])  #разные веса монеток
        self.reset()

    def reset(self):        #Сброс позиции монетки

        self.rect.x = random.randint(40, WIDTH-80)
        self.rect.y = random.randint(-600, -100)
        self.weight = random.choice([1, 1, 1, 2, 2, 3])  #случайный вес при респавне

    def update(self):        #Обновление позиции монетки

        self.rect.y += 4
        if self.rect.top > HEIGHT:
            self.reset()

player = Player()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(player)

for _ in range(5): #враги
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

for _ in range(3): #монетки
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #обновление 
    #print(pygame.key.get_pressed())  

    player.update()

    enemies.update(enemies)
    coins.update()

    #отрисовка
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    #отображение счета
    score_text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH-150, 10))
    
    #отображение текущей скорости врагов
    speed_level = score // coins_to_increase_speed
    speed_text = font.render(f"Speed: {speed_level}", True, (0, 0, 0))
    screen.blit(speed_text, (WIDTH-150, 40))

    #проверка столкновений с врагами
    if pygame.sprite.spritecollide(player, enemies, False):
        pygame.time.delay(2000)
        running = False

    #проверка сбора монеток
    for coin in pygame.sprite.spritecollide(player, coins, True):
        score += coin.weight  #увеличиваем счет на вес монетки
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()