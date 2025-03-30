import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Tool")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK  # Текущий цвет рисования

running = True
mode = "circle"  # Начальный режим рисования

screen.fill(WHITE)  # Заливка фона белым цветом
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "triangle_right"
            elif event.key == pygame.K_e:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_d:
                mode = "rhombus"
            elif event.key == pygame.K_x:
                mode = "eraser"

            # Изменение цвета
            elif event.key == pygame.K_1:
                current_color = RED
            elif event.key == pygame.K_2:
                current_color = GREEN
            elif event.key == pygame.K_3:
                current_color = BLUE

        # Проверка нажатия левой кнопки мыши
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            
            if mode == "circle":
                pygame.draw.circle(screen, current_color, (x, y), 10)
            elif mode == "rect":
                pygame.draw.rect(screen, current_color, (x, y, 30, 20))
            elif mode == "square":
                pygame.draw.rect(screen, current_color, (x, y, 20, 20))
            elif mode == "triangle_right":
                pygame.draw.polygon(screen, current_color, [(x, y), (x, y + 30), (x + 30, y + 30)])
            elif mode == "equilateral_triangle":
                height = int(math.sqrt(3) / 2 * 40)  # Высота равностороннего треугольника
                pygame.draw.polygon(screen, current_color, [(x, y), (x - 20, y + height), (x + 20, y + height)])
            elif mode == "rhombus":
                pygame.draw.polygon(screen, current_color, [(x, y), (x - 20, y + 20), (x, y + 40), (x + 20, y + 20)])
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, (x, y), 15)
    
    pygame.display.flip()

pygame.quit()