import pygame # для работы с графикой
import math # sqrt abs

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()

win_x = 500
win_y = 500
win = pygame.display.set_mode((win_x, win_y)) # Создаём окно
pygame.display.set_caption('Paint') 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Drawing:
    def __init__(self):
        self.color = BLACK  # первый цвет по умолчанию
        self.rad = 6  
        self.mode = "PENCIL"   # режим рисования по умолчанию
        self.start_pos = None   # начальная точка для фигур
        self.is_drawing = False #  рисует ли пользователь фигуру сейчас

    def draw(self, win, pos):
        if self.mode == "PENCIL":
            pygame.draw.circle(win, self.color, pos, self.rad)
        elif self.mode == "ERASER":
            pygame.draw.circle(win, WHITE, pos, 20)  

    def click(self, win, color_buttons, tool_buttons):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]: 
            if pos[0] < 400 and pos[1] > 25:  # Check if inside drawing area
                if self.mode in ["PENCIL", "ERASER"]:
                    self.draw(win, pos)
                elif self.mode in ["RECTANGLE", "CIRCLE", "SQUARE", "RIGHT_TRIANGLE", "EQUILATERAL_TRIANGLE", "RHOMBUS"]:
                    if not self.is_drawing:
                        self.start_pos = pos # запоминаем начальную точку
                        self.is_drawing = True
            else:  # Check if a button was clicked
                for button in color_buttons:
                    if button.is_clicked(pos):
                        self.color = button.color2  

                for button in tool_buttons:
                    if button.is_clicked(pos):
                        if button.action == "CLEAR":
                            win.fill(WHITE)
                        elif button.action == "SMALLER" and self.rad > 2:
                            self.rad -= 1
                        elif button.action == "BIGGER" and self.rad < 20:
                            self.rad += 1
                        elif button.action in ["PENCIL", "RECTANGLE", "CIRCLE", "ERASER", "SQUARE", "RIGHT_TRIANGLE", "EQUILATERAL_TRIANGLE", "RHOMBUS"]:
                            self.mode = button.action

        elif self.is_drawing and self.start_pos and self.mode in ["RECTANGLE", "CIRCLE", "SQUARE", "RIGHT_TRIANGLE", "EQUILATERAL_TRIANGLE", "RHOMBUS"]:
            end_pos = pos
            temp_surface = pygame.Surface((win_x, win_y), pygame.SRCALPHA)  # Temporary surface for preview
            temp_surface.fill((0, 0, 0, 0))  # Transparent

            if self.mode == "RECTANGLE":
                width = end_pos[0] - self.start_pos[0]
                height = end_pos[1] - self.start_pos[1]
                pygame.draw.rect(temp_surface, self.color, (self.start_pos[0], self.start_pos[1], width, height), 2)
            
            elif self.mode == "CIRCLE":
                radius = int(((end_pos[0] - self.start_pos[0])**2 + (end_pos[1] - self.start_pos[1])**2) ** 0.5)
                pygame.draw.circle(temp_surface, self.color, self.start_pos, radius, 2)
            
            elif self.mode == "SQUARE":
                side = max(abs(end_pos[0] - self.start_pos[0]), abs(end_pos[1] - self.start_pos[1]))
                pygame.draw.rect(temp_surface, self.color, 
                                (self.start_pos[0], self.start_pos[1], side, side), 2)
            
            elif self.mode == "RIGHT_TRIANGLE":
                points = [
                    self.start_pos,
                    (self.start_pos[0], end_pos[1]),
                    end_pos
                ]
                pygame.draw.polygon(temp_surface, self.color, points, 2)
            
            elif self.mode == "EQUILATERAL_TRIANGLE":
                side = ((end_pos[0] - self.start_pos[0])**2 + (end_pos[1] - self.start_pos[1])**2)**0.5
                height = (3**0.5 / 2) * side
                points = [
                    self.start_pos,
                    (self.start_pos[0] + side, self.start_pos[1]),
                    (self.start_pos[0] + side/2, self.start_pos[1] - height)
                ]
                pygame.draw.polygon(temp_surface, self.color, points, 2)
            
            elif self.mode == "RHOMBUS":
                center_x = (self.start_pos[0] + end_pos[0]) / 2
                center_y = (self.start_pos[1] + end_pos[1]) / 2
                width = abs(end_pos[0] - self.start_pos[0])
                height = abs(end_pos[1] - self.start_pos[1])
                points = [
                    (center_x, self.start_pos[1]),
                    (end_pos[0], center_y),
                    (center_x, end_pos[1]),
                    (self.start_pos[0], center_y)
                ]
                pygame.draw.polygon(temp_surface, self.color, points, 2)

            win.blit(temp_surface, (0, 0))  # Рисунок отображается на окне win с помощью blit и обновляется:
            if not pygame.mouse.get_pressed()[0]:  # If mouse released, finalize the shape
                self.is_drawing = False


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

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('comicsans', 20)
        text_surface = font.render(self.text, True, self.color2)
        win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, 
                                self.y + self.height / 2 - text_surface.get_height() / 2))

    def is_clicked(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height


def drawHeader(win):
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 25))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 25), 2)
    font = pygame.font.SysFont('comicsans', 20)
    win.blit(font.render('Paint', True, (0, 0, 0)), (200, 5))
    win.blit(font.render('Tools', True, (0, 0, 0)), (425, 5))


def draw(win):
    player1.click(win, Buttons_color, Buttons_other)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500), 2)
    pygame.draw.rect(win, WHITE, (400, 0, 100, 500))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500), 2)
    drawHeader(win)
    for button in Buttons_color + Buttons_other:
        button.draw(win)
    pygame.display.update()


def main_loop():
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        draw(win)
        FramePerSec.tick(FPS)
    pygame.quit()


player1 = Drawing()
win.fill(WHITE)

Buttons_color = [
    Button(407, 30, 40, 40, (0, 0, 255), (0, 0, 255)),  
    Button(453, 30, 40, 40, (255, 0, 0), (255, 0, 0)), 
    Button(407, 76, 40, 40, (0, 255, 0), (0, 255, 0)),  
    Button(453, 76, 40, 40, (255, 192, 0), (255, 192, 0))  
]


Buttons_other = [
    Button(407, 122, 86, 40, (201, 201, 201), BLACK, "CLEAR", "Clear"),
    Button(407, 168, 40, 40, (201, 201, 201), BLACK, "SMALLER", "-"),
    Button(453, 168, 40, 40, (201, 201, 201), BLACK, "BIGGER", "+"),
    Button(407, 214, 86, 40, (201, 201, 201), BLACK, "PENCIL", "Pencil"),
    Button(407, 260, 86, 40, (201, 201, 201), BLACK, "RECTANGLE", "Rect"),
    Button(407, 306, 86, 40, (201, 201, 201), BLACK, "CIRCLE", "Circle"),
    Button(407, 352, 86, 40, (201, 201, 201), BLACK, "ERASER", "Eraser"),
    Button(407, 398, 86, 40, (201, 201, 201), BLACK, "SQUARE", "Square"),
    Button(407, 444, 86, 40, (201, 201, 201), BLACK, "RIGHT_TRIANGLE", "R-Triangle"),
    Button(407, 490, 86, 40, (201, 201, 201), BLACK, "EQUILATERAL_TRIANGLE", "E-Triangle"),
    Button(407, 536, 86, 40, (201, 201, 201), BLACK, "RHOMBUS", "Rhombus")
]

main_loop()