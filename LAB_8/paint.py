import pygame # тут импортирование библеотеки pygame оно обычно отвечает за звуки графику и ввод

pygame.init()   # тут инициализация всех модулей Pygame
FPS = 120 # Frames Per Second сколько раз в секунду обновляется экран. сан көп болған сайын плавнее болады 
FramePerSec = pygame.time.Clock() # Создаём объект для контроля FPS, Ограничивать FPS чтобы игра не работала слишком быстро и что бы анимация была плавной  
win_x = 500
win_y = 500
win = pygame.display.set_mode((win_x, win_y)) # создает  окно с заданным 500*500 пиксельным размером 
pygame.display.set_caption('Paint') # Устанавливаем заголовок окна там на название Paint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Drawing:
    #  Класс Drawing (отвечает за рисование)
    # Когда мы создаём объект класса Drawing
    # вызывается __init__
    def __init__(self): # self нужен, чтобы установить свойства конкретного объекта.
        # self — это ссылка на сам объект
        self.color = BLACK  #хранит текущий цвет (изменяется при нажатии на цветные кнопки).  
        self.rad = 6  # Радиус кисти (толщина линии)
        self.mode = "PENCIL"  # текущий инструмент (PENCIL, ERASER, RECTANGLE, CIRCLE).
        self.start_pos = None # запоминает начальную точку при рисовании фигур. Типа қазір деген жай сызу никакой не тригольник не круг
        self.is_drawing = False # егер прямоугольник, тригольник или т.д бір фигураның біреуін таңдасаң ғана True болады 

    def draw(self, win, pos): # draw() — рисует точки (карандаш/ластик) self нужен, чтобы установить свойства конкретного объекта.
        # win — поверхность, на которой рисуем.
        # pos — координаты центра круга (текущая позиция мыши).
        if self.mode == "PENCIL":
            pygame.draw.circle(win, self.color, pos, self.rad) # Рисуем круг цветом self.color
        elif self.mode == "ERASER":
            pygame.draw.circle(win, WHITE, pos, 20)  # Рисуем белый круг (стираем)
        # pygame.draw.circle - рисует круг
    # click() — обработка кликов мыши
    def click(self, win, color_buttons, tool_buttons):
        pos = pygame.mouse.get_pos() #— возвращает кортеж (x, y) с позицией курсора. Получаем текущие координаты мыши. Эти координаты сохраняются в переменную pos.
        # Проверяем, нажата ли левая кнопка мыши
        if pygame.mouse.get_pressed()[0]: 
            # Проверяем, находится ли курсор в области рисования (x < 400 и y > 25)
            if pos[0] < 400 and pos[1] > 25:
                if self.mode in ["PENCIL", "ERASER"]:
                    """
                    Для карандаша рисует круг текущим цветом (self.color)
                    Для ластика рисует белый круг (стирает)
                    """
                    self.draw(win, pos)
                elif self.mode in ["RECTANGLE", "CIRCLE"]:
                    
                    if not self.is_drawing:
                        self.start_pos = pos # Запоминаем начальную точку
                        self.is_drawing = True  # Начинаем рисование фигуры
            else:
                # Если клик был НЕ в области рисования (значит, по кнопкам)
                # Проверяем цветные кнопки
                for button in color_buttons: 
                    if button.is_clicked(pos):
                        self.color = button.color2  # Меняем цвет рисования
# Если клик был по кнопке (is_clicked(pos)), меняем self.color на цвет кнопки
                for button in tool_buttons:
                    if button.is_clicked(pos):
                        if button.action == "CLEAR":
                            win.fill(WHITE) # Заливаем холст белым
                        elif button.action == "SMALLER" and self.rad > 2:
                            self.rad -= 1 # Уменьшаем размер кисти
                        elif button.action == "BIGGER" and self.rad < 20: # Проверяем, чтобы размер не превысил 20
                            self.rad += 1 # Увеличение размера кисти
                        elif button.action in ["PENCIL", "RECTANGLE", "CIRCLE", "ERASER"]:
                            self.mode = button.action # Меняем self.mode на выбранный инструмент

        elif self.is_drawing and self.start_pos and self.mode in ["RECTANGLE", "CIRCLE"]:
            """Был ли начат процесс рисования (self.is_drawing)
            Есть ли начальная точка (self.start_pos) 
            Выбран ли режим рисования фигур"""
            end_pos = pos #  Текущая позиция - конечная точка фигуры
            if self.mode == "RECTANGLE":
                width = end_pos[0] - self.start_pos[0]
                height = end_pos[1] - self.start_pos[1]
                pygame.draw.rect(win, self.color, (self.start_pos[0], self.start_pos[1], width, height), 2) # Рисуем прямоугольник с рамкой толщиной 2 пикселя
            elif self.mode == "CIRCLE":
                # Вычисляем радиус (расстояние между начальной и текущей точкой)
                radius = int(((end_pos[0] - self.start_pos[0])**2 + (end_pos[1] - self.start_pos[1])**2) ** 0.5)
                pygame.draw.circle(win, self.color, self.start_pos, radius, 2) # Рисуем круг с рамкой толщиной 2 пикселя
            self.is_drawing = False # Сбрасываем флаг рисования Рисование завершено, можно начинать новую фигуру

class Button:
    def __init__(self, x, y, width, height, color, color2, action=None, text=''):
        self.x = x          # Координата X верхнего левого угла
        self.y = y          # Координата Y верхнего левого угла
        self.width = width  # Ширина кнопки
        self.height = height # Высота кнопки
        self.color = color  # Цвет фона кнопки
        self.color2 = color2 # Цвет текста
        self.action = action # Действие при нажатии
        self.text = text    # Текст на кнопке

    def draw(self, win): #  отрисовывает кнопку
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) #бул деген жанагы eraser rect дегендерди шыгару  
        font = pygame.font.SysFont('comicsans', 20) # Название шрифта (используется системный Comic Sans)
        text_surface = font.render(self.text, True, self.color2) # создаёт поверхность с текстом
        win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2,     # размещает текст по центру кнопки центрирует текст на самой кнопке типо анау eraser rect  деген ортасында турады 
                                self.y + self.height / 2 - text_surface.get_height() / 2))

    def is_clicked(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height  # is_clicked для класса, который проверяет, был ли клик на прямоугольной области
    #По горизонтали: self.x < mouse_x < self.x + self.width
    #По вертикали: self.y < mouse_y < self.y + self.height

def drawHeader(win):
    # 1. Рисуем серую полосу заголовка
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 25)) # светло-серый (175, 171, 171)
    # 2. Рисуем чёрные рамки
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2) # Левая часть
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 25), 2) # Правая часть
    # 3. Создаём шрифт
    font = pygame.font.SysFont('comicsans', 20)
    # 4. размещаем текст
    win.blit(font.render('Paint', True, (0, 0, 0)), (200, 5)) # Надпись "Paint" font.render создаёт изображение текста,
    win.blit(font.render('Tools', True, (0, 0, 0)), (425, 5)) # Надпись "Tools"


def draw(win):
    # Обработка действий пользователя
    player1.click(win, Buttons_color, Buttons_other)
    # Отрисовка правой панели инструментов (граница)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500), 2)
    # Заливка правой панели белым
    pygame.draw.rect(win, WHITE, (400, 0, 100, 500))
    # Отрисовка левой панели (холста) с границей
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500), 2)
    # Отрисовка заголовка
    drawHeader(win)
    # Это объединение двух списков:
    for button in Buttons_color + Buttons_other: # кнопки выбора цвета + кнопки с инструментами
        button.draw(win) #win — это окно, куда всё рисуется.
    pygame.display.update()
#После того как все кнопки нарисованы, эта строка обновляет экран.
#Без неё изменения не будут видны пользователю.



def main_loop(): # главный цикл игры или приложения. Внутри него всё работает
    run = True # Пока run = True, программа будет крутиться в бесконечном цикле.
    while run: # Это сам бесконечный цикл, который работает, пока не нажмёшь ESC или не закроешь окно. 
        keys = pygame.key.get_pressed() #Эта строка получает информацию о всех нажатых клавишах на клавиатуре в текущий момент.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: # если пользователь нажал тскапе или икс  тогда run = False
                run = False
        draw(win) # draw(win) — она отвечает за отрисовку всего интерфейса: кнопок, панели инструментов
        FramePerSec.tick(FPS) #Это ограничение количества кадров в секунд
    pygame.quit() # егер run = False болса сразу жабылады


player1 = Drawing() # создается объект player1 из класса Drawing() цвет инструмент 
win.fill(WHITE)

Buttons_color = [
    Button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255)),    # синяя 
    Button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0)),    # красная
    Button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0)),    # зелёная
    Button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0)) # жёлтая 
]



Buttons_other = [
    Button(407, 122, 86, 40, (201, 201, 201), BLACK, "CLEAR", "Clear"), # 407=Горизонтальная позиция кнопки (слева направо) 122=Вертикальная позиция (сверху вниз) 86=Ширина кнопки (в пикселях) 4=Высота кнопки (в пикселях) (201, 201, 201)=цвет фона BLACК =3Цвет текста на кнопке
    Button(407, 168, 40, 40, (201, 201, 201), BLACK, "SMALLER", "-"),
    Button(453, 168, 40, 40, (201, 201, 201), BLACK, "BIGGER", "+"),
    Button(407, 214, 86, 40, (201, 201, 201), BLACK, "PENCIL", "Pencil"),
    Button(407, 260, 86, 40, (201, 201, 201), BLACK, "RECTANGLE", "Rect"),
    Button(407, 306, 86, 40, (201, 201, 201), BLACK, "CIRCLE", "Circle"),
    Button(407, 352, 86, 40, (201, 201, 201), BLACK, "ERASER", "Eraser")
]

main_loop() # Запускает главный цикл,

