import pygame
import os

# Инициализация pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Список треков
storage = ["resources/Michael.mp3", "resources/Minaji.mp3", "resources/music.mp3"]
cur = 0

def play_music():
    """Проигрывает текущий трек"""
    pygame.mixer.music.stop() 
    
    if not os.path.exists(storage[cur]):
        print(f"Ошибка: Файл '{storage[cur]}' не найден!")
        return

    pygame.mixer.music.load(storage[cur])
    pygame.mixer.music.play(-1)

# Создание окна
screen = pygame.display.set_mode((840, 750))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

# Загрузка изображения
controls_img = pygame.image.load("resources/cntrls.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Play
                play_music()
            elif event.key == pygame.K_RIGHT:  # Next
                cur = (cur + 1) % len(storage)
                play_music()
            elif event.key == pygame.K_LEFT:  # Previous
                cur = (cur - 1) % len(storage)
                play_music()
            elif event.key == pygame.K_SPACE:  # Pause/Unpause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    # Отображение интерфейса
    screen.fill((255, 255, 255))
    screen.blit(controls_img, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
