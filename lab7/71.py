import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

# Загрузка изображений
minutes = pygame.image.load("resources/rightarm.png")
seconds = pygame.image.load("resources/sz.png")
casy = pygame.image.load("resources/clock1.png").convert()

# Масштабирование
scaled_sec = pygame.transform.scale(seconds, (seconds.get_width() * 1.4, seconds.get_height() * 1.4))
scaled_min = pygame.transform.scale(minutes, (minutes.get_width() * 1.4, minutes.get_height() * 1.4))

# Центр вращения стрелок
pivot = (539, 508)

# Углы вращения
angle_sec = 0
angle_min = 0

def rotate_around_pivot(image, angle, pivot):
    """Вращает изображение вокруг заданной точки"""
    rotated_image = pygame.transform.rotate(image, -angle)  # Отрицательный угол для часовой стрелки
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление углов
    angle_sec += 0.1  # 6 градусов в секунду (360 / 60)
    angle_min += 0.1 / 60  # 6 градусов в минуту (360 / 60)

    # Вращение стрелок
    rotated_sec, rotated_sec_rect = rotate_around_pivot(scaled_sec, angle_sec, pivot)
    rotated_min, rotated_min_rect = rotate_around_pivot(scaled_min, angle_min, pivot)

    # Отрисовка
    screen.fill((255, 255, 255))
    screen.blit(casy, (-200, 0))
    screen.blit(rotated_sec, rotated_sec_rect.topleft)
    screen.blit(rotated_min, rotated_min_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
