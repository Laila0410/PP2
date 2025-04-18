import pygame
import os  # помощью можно работать операции с файловой системой, управлять процессами, работать с путями,

# Инициализация pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
#44100 это типа качество музыки -16 это как битность звука  2 это как каличество аудиоканалов типа левый правый   512 размер аудиобуфера оно с задержкой работает 
# Список треков
storage = ["resour/Michael.mp3", "resour/Minaji.mp3", "resour/music.mp3"]
cur = 0 # начинает с первой музыки  

def play_music():
    """Проигрывает текущий трек"""
    pygame.mixer.music.stop() 
    # ну это типа если сразу играет музыка то оно останавливает 
    if not os.path.exists(storage[cur]):
        # os.path.exists(storage[cur]): проверяет есть ли путь к текущему треку 
        print(f"Ошибка: Файл '{storage[cur]}' не найден!")
        # если нет то музыка не работает 
        return

    pygame.mixer.music.load(storage[cur])
    # если есть то загружаем файл в память 
    pygame.mixer.music.play(-1)
    #  только  тепреь оно запускается  (-1) это типа играть эту музыку бесконечно 

# Создание окна
screen = pygame.display.set_mode((840, 750))
# создаем окно с размером 840x750 
pygame.display.set_caption("Music Player")
# даем окно название  Music Player
clock = pygame.time.Clock()
# переменная clock что бы окно работала плавно

controls_img = pygame.image.load("resour/cntrls.png")
# тут уже картика с cntrls загружаем его
running = True
while running:
# тут музыка  играетт пока running не станет  False 
    for event in pygame.event.get():
        # for  проходит по каждому событию
        if event.type == pygame.QUIT:
            running = False
        # тут уже проверяем хочк ли я закрыть окно QUIT если я нажимаю на крестик 
        elif event.type == pygame.KEYDOWN:
        # тут если уже мы нажали одну из клавиш клавиатуре, проверяем какую именно клавишу он нажал 
            if event.key == pygame.K_RETURN:  # Play
                # елси pygame.K_RETURN то значит нажана на enter
                play_music()
            elif event.key == pygame.K_RIGHT:  # Next
                cur = (cur + 1) % len(storage)
                # тут типа мой индекс увеличивается на 1 и дальше с того место начинаем
                #  % len(storage) если уже все треки исполнены то начинаем занова
                play_music()
            elif event.key == pygame.K_LEFT:  # Previous
                cur = (cur - 1) % len(storage)
                #  % len(storage) если уже все треки исполнены то cur уменьшается на 1
                play_music()
            elif event.key == pygame.K_SPACE:  # Pause/Unpause
                # если нажато на пробел то pygame.K_SPACE это с рабатовает
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    # Отображение интерфейса
    screen.fill((255, 255, 255))
    # очищает экран, заливая его ...  это нужно что бы удалить старые изображение чтобы тпотом наррисовать новые 
    screen.blit(controls_img, (0, 0))
    # Отображаем изображение на экране или поверхности  ты просто «переносишь» изображение на экран
    pygame.display.flip()
    # pygame.display.flip() = оно не  показывает не покажет изменения (мысалы, нажатие кнопок).
    # Он только обновляет картинку на экране, 
    clock.tick(60)
    # без него 	Цикл выполняется слишком быстро, а с ним играет 60 раз в секунду
pygame.quit()
