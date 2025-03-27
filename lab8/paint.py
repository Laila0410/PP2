import pygame

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Переменные
running = True
current_color = BLACK  # Цвет кисти
mode = "brush"  # brush, rect, circle, eraser
start_pos = None  # Начальная точка для прямоугольников и кругов

# Очистка экрана
screen.fill(WHITE)

# Интерфейс
font = pygame.font.Font(None, 24)
brush_button = pygame.Rect(10, 10, 80, 30)
rect_button = pygame.Rect(100, 10, 80, 30)
circle_button = pygame.Rect(190, 10, 80, 30)
eraser_button = pygame.Rect(280, 10, 80, 30)
color_buttons = [
    (pygame.Rect(370, 10, 30, 30), BLACK),
    (pygame.Rect(410, 10, 30, 30), RED),
    (pygame.Rect(450, 10, 30, 30), GREEN),
    (pygame.Rect(490, 10, 30, 30), BLUE)
]

pygame.display.flip()

while running:
    screen.fill(WHITE, (0, 0, WIDTH, 50))  # Очистка области интерфейса
    pygame.draw.rect(screen, BLACK, brush_button, 2)
    pygame.draw.rect(screen, BLACK, rect_button, 2)
    pygame.draw.rect(screen, BLACK, circle_button, 2)
    pygame.draw.rect(screen, BLACK, eraser_button, 2)
    screen.blit(font.render("Brush", True, BLACK), (brush_button.x + 15, brush_button.y + 7))
    screen.blit(font.render("Rect", True, BLACK), (rect_button.x + 20, rect_button.y + 7))
    screen.blit(font.render("Circle", True, BLACK), (circle_button.x + 10, circle_button.y + 7))
    screen.blit(font.render("Eraser", True, BLACK), (eraser_button.x + 10, eraser_button.y + 7))
    
    for rect, color in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if brush_button.collidepoint(event.pos):
                mode = "brush"
            elif rect_button.collidepoint(event.pos):
                mode = "rect"
            elif circle_button.collidepoint(event.pos):
                mode = "circle"
            elif eraser_button.collidepoint(event.pos):
                mode = "eraser"
            for rect, color in color_buttons:
                if rect.collidepoint(event.pos):
                    current_color = color
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rect":
                end_pos = event.pos
                rect_width = abs(end_pos[0] - start_pos[0])
                rect_height = abs(end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), rect_width, rect_height), 2)
            elif mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                if mode == "brush":
                    pygame.draw.circle(screen, current_color, event.pos, 5)
                elif mode == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, 10)
    
    pygame.display.flip()

pygame.quit()
