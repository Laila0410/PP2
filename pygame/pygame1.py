"""
import pygame
import sys
from  pygame2 import Button
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
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0,5)
    pygame.mier.musicc.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    screen.fill(yellow)
    pygame.display.flip()
run()
"""
import pygame
import sys

# Удален проблемный импорт pygame2

# Цвета
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
    pygame.mixer.music.load(r"C:\Users\Huawei\OneDrive\Desktop\PP2\pygame\maha.mp3")
    pygame.mixer.music.set_volume(0.5)  # Исправлено: запятая заменена на точку
    pygame.mixer.music.play(-1)  # Исправлено: mier -> mixer, musicc -> music
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(black)
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

run()

