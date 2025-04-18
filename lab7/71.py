import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
# нужен что бы играла не работала слишком быстро 
# Загрузка изображений
minutes = pygame.image.load("resour/rightarm.png")
seconds = pygame.image.load("resour/sz.png")
casy = pygame.image.load("resour/clock1.png").convert()

# Масштабирование
scaled_sec = pygame.transform.scale(seconds, (seconds.get_width() * 1.4, seconds.get_height() * 1.4))   #pygame.transform.scale
scaled_min = pygame.transform.scale(minutes, (minutes.get_width() * 1.4, minutes.get_height() * 1.4))

# Центр вращения стрелок
pivot = (508, 508)
# Углы вращения
angle_sec = 0
angle_min = 0

def rotate_around_pivot(image, angle, pivot):
    """Вращает изображение вокруг заданной точки"""
    rotated_image = pygame.transform.rotate(image, -angle)  # Отрицательный угол для часовой стрелки
    # поворачивает изображение против чвсовой стрелки 
    rotated_rect = rotated_image.get_rect(center=pivot)
    # rotated_rect это его новое положение
    # оно типа делает так чтобы центр вращение совпадал 
    return rotated_image, rotated_rect
# rect — это прямоугольник (rectangle) он помагает перемешать и проверять столкновения объектов.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # event это типо нажимаешь клавишу, двигаешь мышку или закрываешь окно,
    # Обновление углов
    angle_sec += 0.1  # 6 градусов в секунду (360 / 60)
    angle_min += 0.1 / 60  # 6 градусов в минуту (360 / 60)

    # Вращение стрелок
    rotated_sec, rotated_sec_rect = rotate_around_pivot(scaled_sec, angle_sec, pivot)
    rotated_min, rotated_min_rect = rotate_around_pivot(scaled_min, angle_min, pivot)
    # rotate_around_pivot() поворачивает изображение angle_sec и angle_min
    # Отрисовка
    screen.fill((255, 255, 255))
    screen.blit(casy, (-200, 0))
    screen.blit(rotated_sec, rotated_sec_rect.topleft)
    screen.blit(rotated_min, rotated_min_rect.topleft)
    # blit часто используется  для рисования одного изображения поверх другого.
    pygame.display.flip() # это метод, который обновляет экран, отображая все изменения, которые были сделаны в текущем фрейме.
    clock.tick(60)

pygame.quit()
