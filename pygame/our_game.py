import pygame
import sys
from pygame2 import Button  # Проверь, существует ли Button в pygame2.py
from image import Pic

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 251)
green = (0, 255, 0)
red = (255, 0, 0)

def run():
    pygame.init()
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("test gaming")

    # Загрузка музыки
    pygame.mixer.music.load('maha.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    running = True
    music_paused = False  # Флаг для паузы
    button = Button(x=screen_width//2 - 75, y=20, width=150, height=50, text='PAUSE')

    start_ticks = pygame.time.get_ticks()  # Начальное время

    while running:
        screen.fill(yellow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event):
                    if music_paused:
                        pygame.mixer.music.unpause()
                        button.text = 'PAUSE'
                    else:
                        pygame.mixer.music.pause()
                        button.text = 'UNPAUSE'
                    music_paused = not music_paused

            if event.type == pygame.KEYUP:
                print(f'Pressed the key: {pygame.key.name(event.key)}')

        # Отображение времени
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        font = pygame.font.Font(None, 36)
        time_text = font.render(f"Time: {elapsed_time} sec", True, red)
        screen.blit(time_text, (10, 10))

        # Отрисовка кнопки
        button.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

run()




"""

import pygame
import sys
from  pygame2 import Button
from image import Pic
black = (0,0,0)
white = (255,255,255)
yellow = (255, 255, 251)
green = (0, 255, 0)
red = (255, 0, 0)
def run():
    pygame.init()
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("test gaming")
    pygame.mixer.music.load('maha.mp3')
    pygame.mixer.music.set_volume(0,5)
    pygame.mier.musicc.play(-1)
    music_paused = False
    running = True
    button = Button(x = screen_width//2 - 75, y = 20 , width =150, height = 50, text = 'PAUSE')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if button.is_clicked(event):
            if music_paused:
                  pygame.mixer.music.unpause()
                  button.text = 'PAUSE'
            else:
                pygame.mixer.music.unpause()
                button.text = 'UNPAUSE'
        if event.type == pygame.KEYUP:
            if event.key == pygame.KEYUP:
                print(f'Pressed thr keyword:{pygame.key.name(event.key)}')
    elapsed_time = (pygame.time_ticks - start_ticket) // 1000
    font = pygame.font.Font(None, 36)
    #time_next = font.render(f"Time:"{elapsed_time}sec" , True, RED)"
    screen.blit(time)
    pic = Pic(screen)
    screen.fill(yellow)

    screen.fill(yellow)
    pygame.mixer.music.stop()
    pygame.mixer.music.pause()
    pygame.display.flip()
    pic.output()
    button.draw(screen)
    pygame.display.flip()
run()

"""