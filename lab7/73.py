import pygame

pygame.init()
# включаем pygame и он загружает гравику и звуки 
screen = pygame.display.set_mode((490, 490))
# создает окно на 490*490 пикселей 
clock = pygame.time.Clock()
# FPS (Frames Per Second, кадры в секунду) 60 это прям плавное движение если еще больше то оно будет очень медленным 

x, y = 25, 25
# координаты нашего центра круга
radius = 25
# біздің қызыл домалағымыздың радиус размері
step = 20
# на сколько пикселей двигаем наш круг

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    # проверяем какие клавиши нажаты если true  то какой клавиш нажат 
    if pressed[pygame.K_DOWN] and y + radius + step <= 490:
        # y + radius + step <= 490: проверяет не выходит ли круг за границы
        y += step
    if pressed[pygame.K_UP] and y - radius - step >= 0:
        y -= step
    if pressed[pygame.K_RIGHT] and x + radius + step <= 490:
        x += step
    if pressed[pygame.K_LEFT] and x - radius - step >= 0:
        x -= step

    screen.fill((255, 255, 255))
    # screen.fill((255, 255, 255)) оно на самом деле очищает экран белым цветом, чтобы круг не оставлял "следов".
    pygame.draw.circle( screen, (220, 0, 0), (x, y), radius)
    # screen это оно подрозумевает типа круг должен быть внутри screen
    pygame.display.flip()
    # display.flip() обновляет экран
    clock.tick(60)

pygame.quit()
