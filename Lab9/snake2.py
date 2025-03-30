import pygame
import time
import random

# Скорость змейки
snake_speed = 15

# Размер окна
window_x = 720
window_y = 480

# Определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Инициализация Pygame
pygame.init()

# Создание игрового окна
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS
fps = pygame.time.Clock()

# Начальное положение змейки
snake_position = [100, 50]

# Начальное тело змейки
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Список возможных видов еды с весами (очки)
food_types = [(10, white), (20, blue), (30, red)]

# Функция для генерации еды

def spawn_food():
    weight, color = random.choice(food_types)
    return [random.randrange(1, (window_x//10)) * 10,
            random.randrange(1, (window_y//10)) * 10,
            weight, color, time.time()]

food = spawn_food()

# Направление движения

direction = 'RIGHT'
change_to = direction

# Очки
score = 0

# Функция для отображения очков
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score : {score}', True, color)
    game_window.blit(score_surface, (10, 10))

# Функция завершения игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, red)
    game_window.blit(game_over_surface, (window_x//4, window_y//4))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Запрещаем движение в противоположном направлении
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Двигаем змейку
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Логика поедания еды
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food[0] and snake_position[1] == food[1]:
        score += food[2]  # Добавляем очки в зависимости от типа еды
        food = spawn_food()
    else:
        snake_body.pop()
    
    # Если еда не съедена через 5 секунд — создаем новую
    if time.time() - food[4] > 5:
        food = spawn_food()

    # Отрисовка фона
    game_window.fill(black)

    # Отрисовка змейки
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Отрисовка еды
    pygame.draw.rect(game_window, food[3], pygame.Rect(food[0], food[1], 10, 10))

    # Проверка столкновения с границами экрана
    if snake_position[0] < 0 or snake_position[0] > window_x-10 or snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Проверка столкновения с самой собой
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Отображение счета
    show_score(white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)
