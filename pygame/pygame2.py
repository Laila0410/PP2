import pygame
black = (0,0,0)
white = (255,255,255)
yellow = (255, 255, 251)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (51,255,255)

class Button():
    def __init__(self, x, y, width, height, text):
        self.react = pygame.React(x,y,width, height)
        self.text = text
        self.font =  pygame.React(None, 36)
        self.color = red 
        self.rect.top = self.screen_rect.center 
    def draw(self, screen):
        pygame.draw.react(screen, self.color, self.react, border_radius = 10)
        text_surf = self.font.render(self.text, True, green)
        text_react = text_surf.get_react(center = self.rect.center)
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.react.collidepoint(event.pos)
    




"""
import pygame
import os
import time

# Инициализация микшера и pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Список треков
storage = ["resources/try1.ogg ", "resources/try2.ogg", "resources/try3.ogg"]
cur = 0

# Функция для проигрывания музыки
def play_music(cur):
    global storage
    pygame.mixer.music.stop()
    time.sleep(1)
    pygame.mixer.music.load(storage[cur])
    pygame.mixer.music.play(-1)

# Создание экрана
screen = pygame.display.set_mode((840, 750))
pygame.display.set_caption("Music Player")
done = False
clock = pygame.time.Clock()

# Загрузка изображения
controls_img = pygame.image.load("resources/cntrls.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Проверка нажатий клавиш
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_RETURN]:  # Play
        play_music(cur)
        time.sleep(0.2)

    elif pressed[pygame.K_RIGHT]:  # Next
        cur = (cur + 1) % len(storage)
        play_music(cur)
        time.sleep(0.2)

    elif pressed[pygame.K_LEFT]:  # Previous
        cur = (cur - 1) % len(storage)
        play_music(cur)
        time.sleep(0.2)

    elif pressed[pygame.K_SPACE]:  # Pause/Unpause
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        time.sleep(0.2)

    # Отображение изображения
    screen.fill((255, 255, 255))
    screen.blit(controls_img, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""